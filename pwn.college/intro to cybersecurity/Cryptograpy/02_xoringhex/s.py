from pwn import *

# Jalankan proses
p = process(['python3', 'run'])

for i in range(10):
    p.recvuntil(b'The key: ')
    key = int(p.recvline().strip(), 16)

    p.recvuntil(b'Encrypted secret: ')
    cipher = int(p.recvline().strip(), 16)

    decrypted = key ^ cipher
    p.recvuntil(b'Decrypted secret? ')
    p.sendline(hex(decrypted).encode())
    print(i)

print(p.recvall().decode())
