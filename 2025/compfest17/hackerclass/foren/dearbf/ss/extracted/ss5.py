import re
import glob

# Ambil semua file dengan pola secret*.txt
files = glob.glob("secret*.txt")

# Urutkan berdasarkan angka di namanya (misal secret12.txt → 12)
files_sorted = sorted(files, key=lambda f: int(re.search(r"\d+", f).group()))

# Gabungkan isi file
flag = ""
for filename in files_sorted:
    with open(filename, "r", encoding="utf-8", errors="replace") as f:
        flag += f.read().strip()

print(f"\n[+] Flag: {flag}")
