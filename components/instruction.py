"""
Instruction module.

This module contains the Instruction type and methods to create them
dynamically at runtime. All instructions are bundled into one type for
simplicity but achieve specificity with named keyword arguments.

"""

from tools import twosComp, bitLen

INSTR_LEN = 32

class Instruction(object):
    def __init__(self, fromBits):
        self.clearFields()
        self.numOpcode = (fromBits >> (INSTR_LEN - 6)) & 0x3f
        if self.numOpcode not in [0, 1]:
            self.strOpcode = _OPCODES[self.numOpcode]
        if self.numOpcode == 4:
            self.make_beqz(fromBits)
        elif self.numOpcode == 35:
            self.make_lw(fromBits)
        elif self.numOpcode == 38:
            self.make_lf(fromBits)
        elif self.numOpcode == 3:
            self.make_jal(fromBits)
        elif self.numOpcode == 19:
            self.make_jalr(fromBits)
        elif self.numOpcode == 18:
            self.make_jr(fromBits)
        elif self.numOpcode == 2:
            self.make_j(fromBits)
        # R-R
        elif self.numOpcode in [0, 1]:
            if self.numOpcode == 0:
                self.funCode = fromBits & 0x3f
            elif self.numOpcode == 1:
                self.funCode = fromBits & 0x1f
            self.strOpcode = _OPCODES[self.numOpcode][self.funCode]
            if self.strOpcode != 'nop':
                self.s1Reg = (fromBits >> 21) & 0x1f
                self.s2Reg = (fromBits >> 16) & 0x1f
                self.dstReg = (fromBits >> 11) & 0x1f
        # J type
        elif self.numOpcode in [2, 3]:
            self.name = fromBits & 0x3ffffff
            if self.numOpcode == 3:
                self.dstReg = 31
        # Trap
        elif self.numOpcode == 17:
            self.s1Reg = (fromBits >> 21) & 0x1f
            self.funCode = fromBits & 0x1f
        else:
            immVal = fromBits & 0xffff
            if (immVal >> 15) == 1:
                self.immediate = twosComp(immVal, bitLen(immVal))
            else:
                self.immediate = immVal
            self.strOpcode = _OPCODES[self.numOpcode]
            self.s1Reg = (fromBits >> 21) & 0x1f
            self.dstReg = (fromBits >> 16) & 0x1f
        self.srcRegType, self.dstRegType = self.getRegisterTypes()

    def getRegisterTypes(self):
        op = self.strOpcode
        if op == 'trap':
            if self.funCode in [0, 1, 3]:
                return 'g', None
            elif self.funCode in [2]:
                return 'f', None
        else:
            return _REGTYPES[op]

    def clearFields(self):
        self.s1Reg = self.s2Reg = self.funCode = None
        self.name = self.dstReg = None
        self.immediate = None
        self.srcRegType = self.dstRegType = None

    def toString(self):
        return "OP: {0}, Func: {1}, Rs1: {2}, Rs2: {3}, Rd: {4}, Imm: {5}, Name: {6}".format(
            self.strOpcode, self.funCode, self.s1Reg, self.s2Reg, self.dstReg,
            self.immediate, self.name
        )

    def isHalt(self):
        return self.strOpcode == 'trap' and self.funCode == 0

    def make_beqz(self, fromBits):
        self.s1Reg = (fromBits >> 21) & 0x1f
        self.name = fromBits & 0xffff
        if (self.name >> 15) == 1:
            self.name = twosComp(self.name, bitLen(self.name))

    def make_lw(self, fromBits):
        self.s1Reg = (fromBits >> 21) & 0x1f
        self.immediate = fromBits & 0xffff
        self.dstReg = (fromBits >> 16) & 0x1f
        if (self.immediate >> 15) == 1:
            self.immediate = twosComp(self.immediate, bitLen(self.immediate))

    def make_lf(self, fromBits):
        self.s1Reg = (fromBits >> 21) & 0x1f
        self.immediate = fromBits & 0xffff
        self.dstReg = (fromBits >> 16) & 0x1f
        if (self.immediate >> 15) == 1:
            self.immediate = twosComp(self.immediate, bitLen(self.immediate))

    def make_jal(self, fromBits):
        self.dstReg = 31
        self.name = fromBits & 0x3ffffff
        if (self.name >> 25) == 1:
            self.name = twosComp(self.name, bitLen(self.name))

    def make_jalr(self, fromBits):
        self.s1Reg = (fromBits >> 21) & 0x1f
        self.dstReg = 31

    def make_jr(self, fromBits):
        self.s1Reg = (fromBits >> 21) & 0x1f

    def make_j(self, fromBits):
        self.name = fromBits & 0x3ffffff
        if (self.name >> 25) == 1:
            self.name = twosComp(self.name, bitLen(self.name))

_FUNCODES0 = {
    0: 'nop', 32: 'add', 34: 'sub', 36: 'and', 37: 'or', 38: 'xor',
    50: 'movf', 52: 'movfp2i', 53: 'movi2fp'
}

_FUNCODES1 = {
    0: 'addf', 1: 'subf', 2: 'multf', 3: 'divf', 9: 'cvtf2i', 12: 'cvti2f',
    14: 'mult', 15: 'div'
}

_OPCODES = {
    0: _FUNCODES0, 1: _FUNCODES1, 2: 'j', 3: 'jal', 8: 'addi', 4: 'beqz',
    17: 'trap', 18: 'jr', 19: 'jalr', 35: 'lw', 38: 'lf', 43: 'sw', 46: 'sf'
}

_REGTYPES = {
    'add': ('g', 'g'),
    'sub': ('g', 'g'),
    'and': ('g', 'g'),
    'or': ('g', 'g'),
    'xor': ('g', 'g'),
    'movf': ('f', 'f'),
    'movfp2i': ('f', 'g'),
    'movi2fp': ('g', 'f'),
    'addf': ('f', 'f'),
    'subf': ('f', 'f'),
    'multf': ('f', 'f'),
    'divf': ('f', 'f'),
    'cvtf2i': ('f', 'f'),
    'cvti2f': ('f', 'f'),
    'mult': ('f', 'f'),
    'div': ('f', 'f'),
    'j': (None, None),
    'nop': (None, None),
    'jal': (None, 'g'),
    'addi': ('g', 'g'),
    'beqz': ('g', None),
    'jr': ('g', None),
    'jalr': ('g', 'g'),
    'lw': ('g', 'g'),
    'lf': ('g', 'f'),
    'sw': ('g', 'g'),
    'sf': ('g', 'f')
}