
WORDSIZE = 4

from .rstation import RStation

class Memory(object):
    def __init__(self):
        super().__init__()
        self.memory = None

    def loadProgram(self, filename):
        """
        :param filename: The .hex file to load from.
        :return: A bytearray object create from bytes in file.
        """
        with open(filename, 'r') as inputFile:
            inputText = inputFile.readlines()
        octets = []
        for line in inputText:
            split = line.split(None, 2)
            data = split[1]

            for i in range(0, len(data), 2):
                octet = int(data[i:i+2], 16)
                octets.append(octet)
        self.memory = bytearray(octets)

    def readBytes(self, index, n):
        return self.memory[index:index + n]

    def readWord(self, index):
        bytes = self.readBytes(index, WORDSIZE)
        word = 0
        for b in bytes:
            word = (word << 8) | b
        return word