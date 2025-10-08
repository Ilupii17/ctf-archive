import hashlib
import math
import ast
from Crypto.Cipher import AES
from fpylll import IntegerMatrix, LLL

# --- 1. Membaca dan mem-parsing file output ---
with open('encrypted.txt', 'r') as f:
    lines = f.readlines()

ciphertext_hex = lines[0].strip().split(": ")[1]
mod = int(lines[1].strip().split(": ")[1])
# Parsing list of lists 'a'
a_str = lines[2].strip().split("Given1: ")[1]
a = ast.literal_eval(a_str)
# Parsing list 'b'
b_str = lines[3].strip().split("Given2: ")[1]
b = ast.literal_eval(b_str)

ciphertext = bytes.fromhex(ciphertext_hex)

# --- 2. Mendefinisikan parameter dari skrip chall.py ---
k, n = 64, 128
bound = int(math.sqrt(mod // 2))
C = bound # Faktor penskalaan yang baik

print(f"[*] Modulo (mod): {mod}")
print(f"[*] Scaling Factor (C): {C}")
print(f"[*] Ukuran Lattice: {n + k} x {n + k}")

# --- 3. Membangun matriks T ---
# T adalah matriks k x n dimana T[i][j] = (b[i] * a[i][j]) % mod
T = []
for i in range(k):
    row = [(b[i] * a_ij) % mod for a_ij in a[i]]
    T.append(row)

# --- 4. Membangun matriks basis kisi B ---
# Dimensi matriks adalah m x m, dimana m = n + k
m = n + k
B = IntegerMatrix(m, m)

# Mengisi blok C * I_n (pojok kiri atas)
for i in range(n):
    B[i, i] = C

# Mengisi blok T^T (pojok kanan atas)
# B[i, n+j] = T[j][i]
for i in range(n):
    for j in range(k):
        B[i, n + j] = T[j][i]

# Mengisi blok mod * I_k (pojok kanan bawah)
for i in range(k):
    B[n + i, n + i] = mod

print("[*] Matriks basis kisi berhasil dibuat. Menjalankan LLL...")

# --- 5. Menjalankan algoritma LLL ---
# LLL.reduction akan mengubah matriks B menjadi basis yang tereduksi
LLL.reduction(B)

print("[*] LLL selesai. Mencari kunci privat...")

# --- 6. Ekstraksi kunci dan dekripsi ---
# Vektor terpendek biasanya adalah baris pertama dari basis yang tereduksi.
# Kita perlu memeriksa vektor itu sendiri dan negatifnya.
shortest_vector = B[0]

# Opsi 1: Menggunakan vektor asli
potential_key_1 = []
for i in range(n):
    # s_i = v_i / C
    val = shortest_vector[i] / C
    potential_key_1.append(int(round(val)))

# Opsi 2: Menggunakan vektor negatif
potential_key_2 = []
for i in range(n):
    val = -shortest_vector[i] / C
    potential_key_2.append(int(round(val)))

# --- 7. Verifikasi dan Dekripsi Flag ---
found = False
for i, p_key in enumerate([potential_key_1, potential_key_2]):
    # Kunci yang valid hanya berisi 0 dan 1
    is_valid = all(bit in [0, 1] for bit in p_key)
    
    if is_valid:
        found = True
        print(f"\n[+] Kunci privat yang valid ditemukan dari Opsi {i+1}!")
        # print(f"Private Key: {p_key}")
        
        # Lakukan dekripsi
        aes_key = hashlib.sha256(bytes(p_key)).digest()
        cipher = AES.new(aes_key, AES.MODE_ECB)
        decrypted_padded = cipher.decrypt(ciphertext)
        
        # Hasil dekripsi mungkin memiliki padding, tapi flag akan terbaca jelas.
        print(f"\n✅ Decrypted Flag: {decrypted_padded.decode(errors='ignore')}")
        break

if not found:
    print("\n[-] Gagal menemukan kunci privat. Coba periksa vektor lain dari basis LLL.")
