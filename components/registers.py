from array import array

class _RegisterFile(object):
    def __init__(self):
        self.values = [0] * 32
        self.status = [None] * 32

class GPR(_RegisterFile):
    def aMethod(self):
        pass

class FPR(_RegisterFile):
    def aMethod(self):
        pass


