

def extractBitField(bitString, len, start, end):
        toExtract = end - start
        (bitString >> (len - 6)) & 0x3f
