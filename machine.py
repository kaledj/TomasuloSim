
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
        self.unitContainers = {'IntUnit': IntUnitContainer(config.intUnits, self),
                       'TrapUnit': TrapUnitContainer(config.trapUnits, self),
                       'BranchUnit': BranchUnitContainer(config.branchUnits, self),
                       'MemUnit': MemUnitContainer(config.memUnits, self),
                       'FPUnit': FPUnitContainer(config.fpUnits, self)
        }

        # System stats
        self.PC = 0
        self.cycle = 0
        self.halted = False

    def run(self):
        while not self.halted or self.hasInstruction():
            cdb = self.write()
            self.execute()
            if not self.halted and not self.pendingBranch():
                instr = self.nextInstruction()
                stalled = False if self.issue(instr) else True
                if not instr.isHalt() and not stalled:
                    self.PC += 4
            self.updateRegFiles(cdb)
            self.updateRStations(cdb)
            self.clearRStations()
            self.cycle += 1

    def write(self):
        for unit in self.unitContainers.values():
            cdb = unit.write()
            if cdb:
                return cdb

    def execute(self):
        for unit in self.unitContainers.values():
            unit.execute()

    def issue(self, instr):
        issued = False
        for unit in self.unitContainers.values():
            if unit.issue(instr):
                return True
        return issued

    def updateRegFiles(self, cdb):
        if cdb is None: return
        source, val = cdb
        for x, regStat in enumerate(self.gprFile.status):
            if regStat == source:
                self.gprFile.values[x] = val
                self.gprFile.status[x] = None
        for x, regStat in enumerate(self.fprFile.status):
            if regStat == source:
                self.fprFile.values[x] = val
                self.fprFile.status[x] = None

    def nextInstruction(self):
        return Instruction(self.memory.readWord(self.PC))

    def pendingBranch(self):
        return False

    def updateRStations(self, cdb):
        if cdb:
            for unit in self.unitContainers.values():
                unit.updateRStations(cdb)

    def clearRStations(self):
        for unit in self.unitContainers.values():
            unit.clearRStations()

    def dumpRStations(self):
        dump = [unit.dumpRStations() for unit in self.unitContainers.values()]
        return '\n'.join(dump)

    def hasInstruction(self):
        for unit in self.unitContainers.values():
            if unit.hasInstruction():
                return True
        return False

    def loadProgram(self, filename):
        self.memory.loadProgram(filename)

