from .funitcontainer import FUnitContainer
from ..funits.branchunit import BranchUnit

class BranchUnitContainer(FUnitContainer):
    def __init__(self, configuration, machine):
        super().__init__(configuration, machine)
        self.funits = [BranchUnit() for i in range(self.numUnits)]

    def issue(self, instr):
        if instr.strOpcode not in self.instructions:
            return False
        if not self.hasOpenRStation():
            return False
        self.getOpenRStation().issue(instr)
        return False
