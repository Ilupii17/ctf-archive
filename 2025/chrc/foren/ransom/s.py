import argparse, os, sys, time, hashlib
from datetime import datetime, timezone

try:
    from Crypto.Cipher import AES
except:
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend

def pbkdf2(pw, salt, iters=200000, dklen=32):
    return hashlib.pbkdf2_hmac("sha256", pw.encode(), salt, iters, dklen)

def pkcs7_unpad(b):
    p=b[-1]
    if p==0 or p>16 or b[-p:]!=bytes([p])*p: raise ValueError
    return b[:-p]

def decrypt(key, iv, ct):
    try:
        return AES.new(key, AES.MODE_CBC, iv).decrypt(ct)
    except:
        cipher=Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        return cipher.decryptor().update(ct)+cipher.decryptor().finalize()

def load_lock(path):
    d=open(path,"rb").read()
    return d[:16], d[16:32], d[32:]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--center", type=int, required=True)
    ap.add_argument("--window", type=int, default=3600)
    args=ap.parse_args()
    salt,iv,ct=load_lock(args.file)
    start,end=args.center-args.window,args.center+args.window
    for ts in range(start,end+1):
        key=pbkdf2(str(ts),salt)
        try: pt=pkcs7_unpad(decrypt(key,iv,ct))
        except: continue
        if b"CRHC{" in pt:
            print(f"[+] Found at {ts} ({datetime.utcfromtimestamp(ts)})")
            print(pt.decode(errors="ignore"))
            return
    print("Not found")

if __name__=="__main__":
    main()
