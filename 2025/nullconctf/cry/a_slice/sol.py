from pwn import remote
from math import gcd, isqrt
from Crypto.Cipher import AES

E = 1337
HOST = "52.59.124.14"
PORT = 5103

def read_banner_and_prompt(io):
    # First line is ciphertext hex
    ct_hex = io.recvline().strip().decode()
    # Now read the full prompt line (discard it)
    io.recvline()
    return ct_hex

def enc(io, m: int) -> int:
    io.sendline(f"e:{m}".encode())
    # Read the result line
    line = io.recvline().strip().decode()
    # Read and discard the prompt line
    io.recvline()
    return int(line)

def recover_n(io, samples=10):
    # Use distinct small m; ensure m >= 2 and vary
    vals = []
    for m in range(2, 2 + samples):
        c = enc(io, m)
        # Compute integer difference m^E - c (no mod)
        v = pow(m, E) - c
        vals.append(abs(v))
    n = 0
    for v in vals:
        n = gcd(n, v) if n else v
    # Harden with a couple extra samples if needed
    for m in [1234567, 7654321, 424242, 1337331]:
        c = enc(io, m)
        v = pow(m, E) - c
        n = gcd(n, abs(v))
    return n

def phi_bounds(n: int):
    r = isqrt(n)
    phi_lo = n - 2*r + 1
    phi_hi = n - 1
    return phi_lo, phi_hi

def d_interval_for_k(phi_lo: int, phi_hi: int, k: int, e: int):
    lo = (k*phi_lo + 1 + e - 1) // e
    hi = (k*phi_hi + 1) // e
    return lo, hi

def common_msb_prefix_bits(lo: int, hi: int, need_bits: int):
    # Compute common MSB prefix between lo and hi inclusive
    L = lo.bit_length()
    H = hi.bit_length()
    maxlen = max(L, H)
    prefix = []
    for i in range(maxlen - 1, -1, -1):
        b_lo = (lo >> i) & 1 if i < L else 0
        b_hi = (hi >> i) & 1 if i < H else 0
        if b_lo == b_hi:
            prefix.append(b_lo)
            if len(prefix) == need_bits:
                return prefix
        else:
            break
    raise ValueError("Interval too wide to extract required MSB prefix.")

def derive_aes_key_from_prefix256(prefix256_bits):
    # Implements: int(bin(d)[2:258:2], 2).to_bytes(16, 'big')
    take = prefix256_bits[0::2]  # 128 bits
    key_int = 0
    for b in take:
        key_int = (key_int << 1) | b
    return key_int.to_bytes(16, 'big')

def try_candidates(n: int, e: int, ct_hex: str):
    phi_lo, phi_hi = phi_bounds(n)
    ct = bytes.fromhex(ct_hex)
    for k in range(1, e):
        d_lo, d_hi = d_interval_for_k(phi_lo, phi_hi, k, e)
        try:
            msb256 = common_msb_prefix_bits(d_lo, d_hi, 256)
        except ValueError:
            continue
        key = derive_aes_key_from_prefix256(msb256)
        pt = AES.new(key, AES.MODE_ECB).decrypt(ct)
        if pt.startswith(b"ENO{"):
            return k, key, pt
    return None

def main():
    io = remote(HOST, PORT)
    ct_hex = read_banner_and_prompt(io)
    print(f"[+] Ciphertext: {ct_hex}")
    n = recover_n(io, samples=10)
    print(f"[+] Recovered n ({n.bit_length()} bits)")
    res = try_candidates(n, E, ct_hex)
    if res:
        k, key, pt = res
        print(f"[+] Found key with k={k}: {key.hex()}")
        print(f"[+] Plaintext (raw): {pt!r}")
        # If there is odd padding, try trimming trailing zero/non-printables gracefully
        cleaned = pt.rstrip(b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10")
        print(f"[+] Plaintext (clean): {cleaned.decode(errors='ignore')}")
    else:
        print("[-] No candidate produced ENO{…}. Try more gcd samples or verify e.")

if __name__ == "__main__":
    main()
