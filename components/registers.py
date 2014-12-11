from array import array

NUM_REGISTERS = 32

class _RegisterFile(object):
    def __init__(self):
        self.values = [0] * NUM_REGISTERS
        self.status = [None] * NUM_REGISTERS

class GPR(_RegisterFile):
    def aMethod(self):
        pass

class FPR(_RegisterFile):
    def aMethod(self):
        pass


