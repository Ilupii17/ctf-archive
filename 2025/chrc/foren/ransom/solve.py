#!/usr/bin/env python3
import argparse
import hashlib
from datetime import datetime
from tqdm import tqdm
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def pbkdf2(password: str, salt: bytes, iters: int = 200000, dklen: int = 32) -> bytes:
    """Menghasilkan kunci menggunakan PBKDF2-HMAC-SHA256."""
    return hashlib.pbkdf2_hmac("sha256", password.encode('utf-8'), salt, iters, dklen)

def main():
    parser = argparse.ArgumentParser(description="AES Timestamp Decryptor Sederhana.")
    parser.add_argument("-f", "--file", required=True, help="File .lock yang akan didekripsi.")
    parser.add_argument("-c", "--center", type=int, required=True, help="Unix timestamp sebagai titik tengah pencarian.")
    parser.add_argument("-w", "--window", type=int, default=120, help="Jangkauan pencarian (detik) di sekitar titik tengah.")
    parser.add_argument("-p", "--prefix", default="CRHC{", help="Prefix flag yang diharapkan untuk verifikasi.")
    parser.add_argument("-o", "--output", default="decrypted_file", help="Nama file untuk menyimpan hasil.")
    args = parser.parse_args()

    # 1. Memuat file terenkripsi
    try:
        with open(args.file, "rb") as f:
            salt, iv, ciphertext = f.read(16), f.read(16), f.read()
    except FileNotFoundError:
        print(f"[!] Error: File '{args.file}' tidak ditemukan.")
        return

    start_ts = args.center - args.window
    end_ts = args.center + args.window
    prefix_bytes = args.prefix.encode('utf-8')

    # 2. Loop brute-force dengan progress bar
    for ts in tqdm(range(start_ts, end_ts + 1), desc="Mencari Kunci"):
        try:
            key = pbkdf2(str(ts), salt)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

            # 3. Verifikasi dengan prefix flag
            if plaintext.startswith(prefix_bytes):
                tqdm.write("\n" + "="*40)
                tqdm.write(f"🎉 [+] KUNCI DITEMUKAN PADA TIMESTAMP: {ts}")
                tqdm.write("="*40)
                
                # 4. Simpan hasil dekripsi
                with open(args.output, "wb") as out_file:
                    out_file.write(plaintext)
                tqdm.write(f"💾 Hasil dekripsi disimpan ke: '{args.output}'")
                tqdm.write(f"👉 Langkah selanjutnya, periksa tipe filenya dengan: file {args.output}")
                return
        except ValueError: # Gagal unpadding, berarti kunci salah
            continue
    
    print("\n[!] Kunci tidak ditemukan dalam jangkauan yang diberikan.")

if __name__ == "__main__":
    main()
