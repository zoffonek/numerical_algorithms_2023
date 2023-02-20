import struct
import numpy as np
 
value = np.float32(17.3)
ba = bytearray(struct.pack("f", value))   
 
print([ "0x{:02x}".format(b) for b in ba ])     # ['0x66', '0x66', '0x8a', '0x41']

# ex 4

def float2ByArray(value):
    return bytearray(struct.pack("f", np.float32(value)))

print([ "0x{:02x}".format(b) for b in float2ByArray(12.5) ])
print([ "0x{:02x}".format(b) for b in float2ByArray(-12.5) ])
