from unittest import TestCase

from machine import Machine
from components.instruction import Instruction

class TestMachine(TestCase):
    def test_issue(self):
        machine = Machine()
        instr = Instruction(0x20010003)
        self.assertTrue(machine.issue(instr))
        self.assertTrue(machine.hasInstruction())

        rstations = machine.unitContainers['IntUnit'].dumpRStations()

    def test_nextInstruction(self):
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit1.hex')
        instruc = machine.nextInstruction()

    def test_nextInstructionAndIssue(self):
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit1.hex')
        count = 0
        while True:
            instruc = machine.nextInstruction()
            machine.issue(instruc)
            count += 1
            machine.PC += 4
            if instruc.isHalt():
                break
        self.assertEquals(count, 15)
        rstations = machine.dumpRStations()

    def test_nextInstructionAndIssue(self):
        machine = Machine()
        machine.loadProgram('Tomasulo/memUnit1.hex')
        count = 0
        while True:
            instruc = machine.nextInstruction()
            machine.issue(instruc)
            count += 1
            machine.PC += 4
            if instruc.isHalt():
                break
        self.assertEquals(count, 26)
        rstations = machine.dumpRStations()

    def test_execute(self):
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit1.hex')
        count = 0
        while True:
            instruc = machine.nextInstruction()
            machine.execute()
            machine.issue(instruc)
            count += 1
            machine.PC += 4
            if instruc.isHalt():
                break
        self.assertEquals(count, 15)
        rstations = machine.dumpRStations()

    def test_execute_trap(self):
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit1.hex')
        instruction = Instruction(0x44800003)
        machine.issue(instruction)
        machine.execute()
        machine.execute()


    # def test_run(self):
    #     machine = Machine()
    #     machine.loadProgram('Tomasulo/intUnit1.hex')
    #     machine.run()

    def test_memory(self):
        pass

    def test_machine(self):
        machine = Machine()
