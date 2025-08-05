from Crypto.Util.strxor import strxor

# Menggunakan pasangan pertama dari output yang Anda berikan:
key_hex = "b283fcb038d4eac49ed85478b8924562f802e6b3df14af0c506ec45f7076e36d78bcf15d4e0cdcc11a4a3b0ce32a2f11856f6428be3b6a69c2dd"
ciphertext_hex = "c2f4929e5bbb86a8fbbf3103eda52f209457d3818e42cc66021ca03a4106a9061dc6a6642040ecef7e18414299676b5db7083066c462103ebfd7"

# Ubah string hex menjadi bytes
key = bytes.fromhex(key_hex)
ciphertext = bytes.fromhex(ciphertext_hex)

# Lakukan XOR untuk mendapatkan flag
flag_bytes = strxor(ciphertext, key)

# Cetak flag-nya
print("Flag-nya adalah:")
print(flag_bytes.decode(errors='ignore'))