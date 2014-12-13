"""
Machine

This module implements the highest level of operation logic.

The Machine type contains all subcomponents of the machine. High level
issue, execute, write loop occurs here.

"""

from logger import log
import config
from components import *


class Machine(object):
    def __init__(self):
        self.program = ''
        # Memory and registers
        self.memory = Memory()
        self.gprFile = GPR()
        self.fprFile = FPR()

        # Functional units and rstations
        self.unitContainers = [IntUnitContainer(config.intUnits, self),
                               TrapUnitContainer(config.trapUnits, self),
                               BranchUnitContainer(config.branchUnits, self),
                               MemUnitContainer(config.memUnits, self),
                               FPUnitContainer(config.fpUnits, self)]
        # System stats
        self.PC = 0
        self.cycle = 0
        self.haltIssued = False

    def run(self):
        while not self.haltIssued or self.hasInstruction():
            log('\n\n# Clock cycle: {0} #\n{2}'.format(self.cycle, '#'*20, '#'*20))
            cdb = self.write()
            self.execute()
            if not self.haltIssued and not self.pendingBranch():
                instr = self.nextInstruction()
                stalled = False if self.issue(instr) else True
                if not instr.isHalt() and not stalled:
                    self.PC += 4
            self.updateRegFiles(cdb)
            self.updateRStations(cdb)
            self.clearRStations()
            self.cycle += 1

    def write(self):
        for unit in self.unitContainers:
            cdb = unit.write()
            if cdb:
                return cdb

    def execute(self):
        for unit in self.unitContainers:
            unit.execute()

    def issue(self, instr):
        issued = False
        for unit in self.unitContainers:
            if unit.issue(instr):
                return True
        return issued

    def updateRegFiles(self, cdb):
        if cdb is None: return
        source, val = cdb
        log('Writing: {0} {1} to CDB.'.format(source, val))
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
        for unit in self.unitContainers:
            if type(unit) is BranchUnitContainer:
                return unit.hasInstruction()

    def updateRStations(self, cdb):
        if cdb:
            for unit in self.unitContainers:
                unit.updateRStations(cdb)

    def clearRStations(self):
        for unit in self.unitContainers:
            unit.clearRStations()

    def dumpRStations(self):
        dump = [unit.dumpRStations() for unit in self.unitContainers]
        return '\n'.join(dump)

    def hasInstruction(self):
        for unit in self.unitContainers:
            if unit.hasInstruction():
                return True
        return False

    def loadProgram(self, filename):
        log('Loading program: {0}'.format(filename))
        self.program = filename
        self.memory.loadProgram(filename)

