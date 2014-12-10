
INSTR_LEN = 32

class Instruction(object):
    def __init__(self, fromBits):
        self.clearFields()
        self.numOpcode = (fromBits >> (INSTR_LEN - 6)) & 0x3f
        # R-R
        if self.numOpcode in [0, 1]:
            if self.numOpcode == 0:
                self.funCode = fromBits & 0x3f
                self.regType = 'fpr'
            else:
                self.funCode = fromBits & 0x1f
                self.regType = 'gpr'
            self.strOpcode = _OPCODES[self.numOpcode][self.funCode]
            self.s1Reg = (fromBits >> 21) & 0x1f
            self.s2Reg = (fromBits >> 16) & 0x1f
            self.dstReg = (fromBits >> 11) & 0x1f
        # J type
        elif self.numOpcode in [2, 3]:
            self.name = fromBits & 0x3ffffff
            self.strOpcode = _OPCODES[self.numOpcode]
            self.dstReg = 31
            self.regType = 'gpr'
        # Trap
        elif self.numOpcode == 17:
            self.strOpcode = _OPCODES[self.numOpcode]
            self.trapReg = (fromBits >> 21) & 0x1f
            self.funCode = fromBits & 0x1f
            if self.funCode == 2:
                self.regType = 'fpr'
            else:
                self.regType = 'gpr'
        else:
            self.immediate = fromBits & 0xffff
            self.strOpcode = _OPCODES[self.numOpcode]
            self.s1Reg = (fromBits >> 21) & 0x1f
            self.dstReg = (fromBits >> 16) & 0x1f
            self.regType = 'gpr'

    def clearFields(self):
        self.s2Reg = self.funCode = None
        self.name = self.s1Reg = self.dstReg = None
        self.immediate = None

    def toString(self):
        return "OP: {0}, Func: {1}, Rs1: {2}, Rs2: {3}, Rd: {4}, Imm: {5}, Name: {6}".format(
            self.strOpcode, self.funCode, self.s1Reg, self.s2Reg, self.dstReg,
            self.immediate, self.name
        )

    def isHalt(self):
        return self.strOpcode == 'trap' and self.funCode == 0


_FUNCODES0 = {
    0: 'nop',
    32: 'add',
    34: 'sub',
    36: 'and',
    37: 'or',
    38: 'xor',
    50: 'movf',
    52: 'movfp2i',
    53: 'movi2fp'
}

_FUNCODES1 = {
    0: 'addf',
    1: 'subf',
    6: 'multf',
    7: 'divf',
    9: 'cvtf2i',
    12: 'cvti2f',
    14: 'mult',
    15: 'div'
}

_OPCODES = {
    0: _FUNCODES0,
    1: _FUNCODES1,
    2: 'j',
    3: 'jal',
    8: 'addi',
    4: 'beqz',
    17: 'trap',
    18: 'jr',
    19: 'jalr',
    35: 'lw',
    38: 'lf',
    43: 'sw',
    46: 'sf'
}
