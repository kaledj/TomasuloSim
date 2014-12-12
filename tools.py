import struct

def twosComp(val, bits):
    if val & (1 << (bits - 1)) != 0:
        val -= 1 << bits
    return val

def bitLen(value):
    length = 0
    while value:
        length += 1
        value >>= 1
    return length

def bitsAsFloat(intValue):
    return struct.unpack('>f', struct.pack('>I', intValue))[0]


def floatAsBits(floatValue):
    return struct.unpack('>I', struct.pack('>f', floatValue))[0]