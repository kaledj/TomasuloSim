from unittest import TestCase

from machine import Machine
from components.instruction import Instruction

class TestMachine(TestCase):
    def test_issue(self):
        machine = Machine()
        instr = Instruction(0x20010003)
        self.assertTrue(machine.issue(instr))
        self.assertTrue(machine.hasInstruction())

        rstations = machine.FUnits['IntUnit'].dumpRStations()
        print(rstations)

    def test_nextInstruction(self):
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit1.hex')
        instruc = machine.nextInstruction()

    def test_nextInstructionAndIssue(self):
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit1.hex')
        while True:
            instruc = machine.nextInstruction()
            machine.issue(instruc)
            machine.PC += 4
            if instruc.isHalt():
                break

    def test_memory(self):
        pass

    def test_machine(self):
        machine = Machine()
