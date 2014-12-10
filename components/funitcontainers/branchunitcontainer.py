from .funitcontainer import FUnitContainer
from ..funits.branchunit import BranchUnit

class BranchUnitContainer(FUnitContainer):
    def __init__(self, configuration, machine):
        super().__init__(configuration, machine)
        self.branchUnits = [BranchUnit() for i in range(self.numUnits)]
