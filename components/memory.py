
import struct
from .rstation import RStation

WORDSIZE = 4

class Memory(object):
    def __init__(self):
        super().__init__()
        self.memory = bytearray()

    def loadProgram(self, filename):
        """
        :param filename: The .hex file to load from.
        :return: A bytearray object create from bytes in file.
        """
        with open(filename, 'r') as inputFile:
            inputText = inputFile.readlines()
        octets = []
        address = 0
        for line in inputText:
            split = line.split(None, 2)
            addressString = split[0][0:-1]
            data = split[1]
            # If current address if behind, pad memory with 0s
            for i in range(0, int(addressString, 16) - address):
                octets.append(0)
                address += 1
            for i in range(0, len(data), 2):
                octet = int(data[i:i+2], 16)
                octets.append(octet)
                address += 1
        self.memory = bytearray(octets)

    def storeBytes(self, address, n, data):
        self.memory[address:address + n] = data

    def storeWord(self, address, word):
        data = bytearray(WORDSIZE)
        data[3] = word & 0xFF
        data[2] = (word >> 8) & 0xFF
        data[1] = (word >> 16) & 0xFF
        data[0] = (word >> 24) & 0xFF
        self.storeBytes(address, WORDSIZE, data)

    def readBytes(self, index, n):
        return self.memory[index:index + n]

    def readByte(self, address):
        return self.memory[address]

    def readWord(self, index):
        dataBytes = self.readBytes(index, WORDSIZE)
        word = 0
        for b in dataBytes:
            word = (word << 8) | b
        return word

    def readFloatWord(self, address):
        dataBytes = self.readBytes(address, WORDSIZE)
        return struct.unpack('>f', dataBytes)[0]

    def readString(self, address):
        terminated = False
        characters = []
        while not terminated:
            byte = self.readByte(address)
            if byte == 0:
                terminated = True
            else:
                characters.append(chr(byte))
            address += 1
        return ''.join(characters)
