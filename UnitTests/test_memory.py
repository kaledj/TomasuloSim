from unittest import TestCase
from components.memory import Memory
import os

class TestMemory(TestCase):
    def test_loadProgram(self):
        mem = Memory()
        for file in os.listdir('Tomasulo'):
            if not file.endswith('.hex'): continue
            mem.loadProgram('Tomasulo/' + file)

    def test_readString(self):
        mem = Memory()
        mem.loadProgram('Tomasulo/intUnit1.hex')
        expected = '\nThe sum of '
        actual = mem.readString(0x3c)
        self.assertEquals(expected, actual)
        expected = ' and '
        actual = mem.readString(0x4a)
        self.assertEquals(expected, actual)
        expected = ' is '
        actual = mem.readString(0x50)
        self.assertEquals(expected, actual)
        expected = '.\n'
        actual = mem.readString(0x55)
        self.assertEquals(expected, actual)

        mem.loadProgram('Tomasulo/brUnit1.hex')
        expected = '\nThe max of '
        actual = mem.readString(0x94)
        self.assertEquals(expected, actual)
        expected = ' and '
        actual = mem.readString(0xa2)
        self.assertEquals(expected, actual)

    def test_storeWord(self):
        mem = Memory()
        mem.loadProgram('Tomasulo/intUnit1.hex')
        mem.storeWord(0, 0xFFFFFFFF)
        self.assertEquals(mem.readWord(0), 0xFFFFFFFF)

    def test_readFloatWord(self):
        mem = Memory()
        mem.loadProgram('Tomasulo/fpUnit4.hex')
        val = mem.readFloatWord(0x44)
