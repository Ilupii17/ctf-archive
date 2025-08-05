from pwn import *

io = process(['python3','run'], stdin=PTY)

for _ in range(1, 10):
    # Tangkap encrypted char (dalam bentuk bytes), lalu decode ke string
    enc_char = io.recvregex(br'- Encrypted Character: (.+)\n', capture=True).group(1).decode()
    key = io.recvregex(br'- XOR Key: (.+)\n', capture=True).group(1).decode()

    # Ubah encrypted char ke karakter, XOR dengan key (dalam integer)
    dec_char = chr(ord(enc_char) ^ int(key, 16))

    # Tunggu prompt, lalu kirim jawaban
    io.recvuntil(b"- Decrypted Character? ")
    io.sendline(dec_char.encode())

    # Cek lanjut
    io.recvline_endswith(b'Moving on.')

# Tangkap flag
flag = io.recvregex(br'.+flag:\n(.+)\n', capture=True).group(1).decode()
print("Flag:", flag)
