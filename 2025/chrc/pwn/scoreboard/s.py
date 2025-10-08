from pwn import *
import sys

key = 0xAA
n = 21
data = bytearray(n)

# 1. Isi 8 byte pertama (s2) - Ini sudah benar
data[0:8] = p64(0xCED89ADDD9D9EAFA)

# 2. Isi 8 byte berikutnya (v4[0]) - Ini sudah benar
data[8:16] = p64(0xDB929FC298CF92F5)

# 3. Lakukan overwrite di offset yang BENAR
#    Offset absolut = 8 (dari s2) + 5 (dari v4) = 13.
#    Slice yang benar adalah dari indeks 13 hingga 20 -> data[13:21]
data[13:21] = p64(0x9FDBDE93DEDB929F) # <-- PERBAIKAN DI SINI

# XOR untuk mendapatkan plaintext password
password = xor(data, key) # pwntools' xor lebih ringkas

print("Password yang benar adalah:")
# Gunakan sys.stdout.buffer.write untuk mencetak byte mentah dengan aman
sys.stdout.buffer.write(password)
print() # Untuk newline