import unittest

from components.instruction import Instruction

class InstructionTest(unittest.TestCase):
    def test_instruction(self):
        instr = Instruction(0x20010003)
        self.assertEquals(instr.s1Reg, 0)
        self.assertEquals(instr.srcRegType, 'g')
        self.assertEquals(instr.dstReg, 1)
        self.assertEquals(instr.dstRegType, 'g')
        self.assertEquals(instr.immediate, 3)

    def test_instruction2(self):
        instr = Instruction(0x44800003)
        self.assertEquals(instr.numOpcode, 17)
        self.assertEquals(instr.strOpcode, 'trap')
        self.assertEquals(instr.funCode, 3)
        self.assertEquals(instr.srcRegType, 'g')
        self.assertEquals(instr.s1Reg, 4)

    def test_instruction3(self):
        instr = Instruction(0x9821ffff)

