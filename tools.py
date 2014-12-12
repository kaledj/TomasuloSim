import struct

# def extractBitField(bitString, len, start, end):
#         toExtract = end - start
#         (bitString >> (len - 6)) & 0x3f

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
    return struct.unpack('>f', struct.pack('>i', intValue))[0]

def floatAsBits(floatValue):
    return struct.unpack('>i', struct.pack('>f', floatValue))[0]