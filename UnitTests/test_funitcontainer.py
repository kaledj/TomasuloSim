from unittest import TestCase

from components.instruction import Instruction
from components.funitcontainers.intunitcontainer import IntUnitContainer
from machine import Machine
import config

class TestFUnitContainer(TestCase):
    def setUp(self):
        self.machine = Machine()

    def test_hasInstruction(self):
        instr = Instruction(0x20010003)
        container = self.machine.FUnits['IntUnit']
        container.issue(instr)
        self.assertTrue(container.hasInstruction())

    def test_issue(self):
        instr = Instruction(0x20010003)
        container = self.machine.FUnits['IntUnit']
        for i in range(container.numRStations):
            container.issue(instr)
        self.assertFalse(container.hasOpenRStation())
        self.assertIsNone(container.getOpenRStation())
        self.assertFalse(container.issue(instr))
