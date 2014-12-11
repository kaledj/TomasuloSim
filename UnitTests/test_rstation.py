from unittest import TestCase
from machine import Machine
from components.instruction import Instruction

class TestRStation(TestCase):
    def setUp(self):
        self.machine = Machine()

    def test_execute(self):
        instr = Instruction(0x20010003)
