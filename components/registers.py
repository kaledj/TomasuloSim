"""
Registers

This module implements registers for the machine. Registers are stored
as collections of integer values. There is a corresponding status field
with each register.

"""

NUM_REGISTERS = 32

class _RegisterFile(object):
    """
    RegisterFile type

    The basic implementation of registers. Provides the necessary functionality.
    """
    def __init__(self):
        self.values = [0] * NUM_REGISTERS
        self.status = [None] * NUM_REGISTERS

class GPR(_RegisterFile):
    def aMethod(self):
        pass

class FPR(_RegisterFile):
    def aMethod(self):
        pass


