#!/usr/bin/env python3
import struct
import pyshark

PCAP = "usbstorage.pcapng"
OUT_GZ = "flag.tar.gz"
SECTOR_SIZE = 512
USBC = b"USBC"  # CBW signature 0x55 53 42 43
USBS = b"USBS"  # CSW signature 0x55 53 42 53
OP_READ10 = 0x28
GZIP_MAGIC = b"\x1f\x8b\x08"

def hexfield(pkt, field):
    try:
        v = getattr(pkt, field).replace(":", "")
        return bytes.fromhex(v)
    except Exception:
        return None

print("[*] Opening capture...")
cap = pyshark.FileCapture(
    PCAP,
    use_json=True,
    include_raw=True,
    keep_packets=False,  # stream to reduce memory
    display_filter="usb.data_len > 0"  # get both directions with data
)

# State for current in-flight READ(10)
pending = None  # dict with keys: tag, lba, total, collected, chunks(list)
chunks_by_lba = []  # list of (lba, data)

def start_read10(tag, lba, blocks, xfer_len):
    return {
        "tag": tag,
        "lba": lba,
        "blocks": blocks,
        "total": xfer_len,
        "collected": 0,
        "buf": bytearray()
    }

def parse_cbw(cbw):
    # struct:
    # dCBWSignature[4], dCBWTag[4], dCBWDataTransferLength[4],
    # bmCBWFlags[1], bCBWLUN[1], bCBWCBLength[1], CBWCB[16]
    if len(cbw) < 31 or cbw[0:4] != USBC:
        return None
    dCBWTag, dCBWDTL = struct.unpack("<II", cbw[4:12])
    bmFlags = cbw[12]
    cdb_len = cbw[14]
    cdb = cbw[15:15+16]
    if cdb_len == 0 or len(cdb) < 10:
        return None
    opcode = cdb[0]
    direction_in = (bmFlags & 0x80) != 0
    return {
        "tag": dCBWTag,
        "xfer_len": dCBWDTL,
        "direction_in": direction_in,
        "opcode": opcode,
        "cdb": cdb
    }

def parse_read10_lba_blocks(cdb):
    # CDB[0]=0x28, LBA = bytes 2..5, Transfer length (blocks) = bytes 7..8
    lba = struct.unpack(">I", cdb[2:6])[0]
    blocks = struct.unpack(">H", cdb[7:9])[0]
    return lba, blocks

print("[*] Scanning packets and reconstructing READ(10) data...")
for pkt in cap:
    # Direction: 0 = host->device (OUT), 1 = device->host (IN)
    try:
        direction = int(pkt.usb.endpoint_address_direction)
    except Exception:
        # some builds expose usb.endpoint_address.direction or none; try both
        try:
            direction = int(pkt.usb.endpoint_address.direction)
        except Exception:
            continue

    data = hexfield(pkt.usb, "capdata")
    if not data:
        continue

    if direction == 0:
        # Possible CBW (host to device) — detect and start READ(10)
        cbw = parse_cbw(data)
        if not cbw:
            continue
        if not (cbw["direction_in"] and cbw["opcode"] == OP_READ10 and cbw["xfer_len"] > 0):
            # Not a READ(10) IN transfer
            continue
        lba, blocks = parse_read10_lba_blocks(cbw["cdb"])
        expected_bytes = blocks * SECTOR_SIZE
        # Some stacks set xfer_len to bytes, others to same expected_bytes for READ(10)
        # Trust the sector math for data phase length.
        pending = start_read10(cbw["tag"], lba, blocks, expected_bytes)
    else:
        # IN data — if we have a pending READ(10), accumulate until satisfied
        if pending and pending["collected"] < pending["total"]:
            take = min(len(data), pending["total"] - pending["collected"])
            pending["buf"].extend(data[:take])
            pending["collected"] += take
            # If there are more bytes than expected (e.g., CSW in same packet tail), ignore extras here.

            if pending["collected"] >= pending["total"]:
                # Completed one READ(10) data phase
                chunks_by_lba.append((pending["lba"], bytes(pending["buf"])))
                pending = None
        else:
            # Not in a data phase we care about — skip
            continue

cap.close()
print(f"[*] Completed READ(10) chunks: {len(chunks_by_lba)}")

if not chunks_by_lba:
    print("[-] No READ(10) data reconstructed. Double-check the capture and filter.")
    exit(1)

# Assemble by LBA
chunks_by_lba.sort(key=lambda x: x[0])
assembled = bytearray()
for lba, blob in chunks_by_lba:
    assembled.extend(blob)

# Search for gzip stream
idx = assembled.find(GZIP_MAGIC)
if idx == -1:
    print("[-] Gzip header not found in assembled data. Writing full assembled.bin for manual carving.")
    with open("assembled.bin", "wb") as f:
        f.write(assembled)
    exit(2)

print(f"[+] Gzip header found at offset {idx} in assembled data.")
with open(OUT_GZ, "wb") as f:
    f.write(assembled[idx:])
print(f"[+] Wrote {OUT_GZ}. Try: file {OUT_GZ} && tar -xvzf {OUT_GZ}")
