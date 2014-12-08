
from logger import log
import config
from components import *

class Machine(object):
    def __init__(self):
        self.memory = Memory()
        self.intUnits = IntUnitContainer(config.intUnits['rStations'],
                                    config.intUnits['numUnits'])
        self.trapUnits = TrapUnitContainer(config.trapUnits['rStations'],
                                    config.trapUnits['numUnits'])
        self.branchUnits = BranchUnitContainer(config.branchUnits['rStations'],
                                    config.branchUnits['numUnits'])
        self.memUnits = MemUnitContainer(config.memUnits['rStations'],
                                    config.memUnits['numUnits'])
        self.fpUnits = FPUnitContainer(config.fpUnits['rStations'],
                                    config.fpUnits['numUnits'])
        self.FUnits = {'IntUnits': self.intUnits,
                       'TrapUnits': self.trapunits,
                       'BranchUnits': self.branchUnits,
                       'MemUnits': self.memUnits,
                       'FPUnits': self.fpUnits}

    def run(self):
        log(self.intUnits.dumpRStations())

    def loadProgram(self, filename):
        self.memory.loadProgram(filename)

