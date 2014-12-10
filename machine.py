
from logger import log
import config
from components import *

class Machine(object):
    def __init__(self):
        # Memory and registers
        self.memory = Memory()
        self.gprFile = GPR()
        self.fprFile = FPR()

        # Functional units and rstations
        self.FUnits = {'IntUnit': IntUnitContainer(config.intUnits, self),
                       'TrapUnit': TrapUnitContainer(config.trapUnits, self),
                       'BranchUnit': BranchUnitContainer(config.branchUnits, self),
                       'MemUnit': MemUnitContainer(config.memUnits, self),
                       'FPUnit': FPUnitContainer(config.fpUnits, self)
        }

        # System stats
        self.PC = 0
        self.halted = False

    def run(self):
        while not self.halted or self.hasInstruction():
            source, value = self.write()
            self.execute()
            if not self.halted and not self.pendingBranch():
                instr = self.nextInstruction()
                stalled = self.issue(instr)
                if instr.isHalt() and not stalled:
                    self.PC += 4
            self.updateRStations(source, value)
            self.clearRStations()

    def write(self):
        pass

    def execute(self):
        pass

    def issue(self, instr):
        issued = False
        for unit in self.FUnits.values():
            if unit.issue(instr):
                return True
        return issued

    def nextInstruction(self):
        return Instruction(self.memory.readWord(self.PC))

    def pendingBranch(self):
        pass

    def updateRStations(self, source, value):
        pass

    def clearRStations(self):
        pass

    def hasInstruction(self):
        for unit in self.FUnits.values():
            if unit.hasInstruction():
                return True
        return False

    def loadProgram(self, filename):
        self.memory.loadProgram(filename)

