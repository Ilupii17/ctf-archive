# Simpan sebagai solver.py
from pwn import *
from Crypto.Util.strxor import strxor
p = process(['python3', './run'])

for n in range(1, 10):
    log.info(f"Menyelesaikan tantangan #{n}...")
    
    p.recvuntil(b"- Encrypted String: ")
    ct_str = p.recvline().strip().decode()

    p.recvuntil(b"- XOR Key String: ")
    key_str = p.recvline().strip().decode()
    
    pt_bytes = strxor(ct_str.encode(), key_str.encode())
    
    p.sendlineafter(b"- Decrypted String? ", pt_bytes)

log.success("Semua tantangan selesai! Menunggu flag...")
flag = p.recvall().decode()
print(flag)