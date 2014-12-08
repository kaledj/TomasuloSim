from .funitcontainer import FUnitContainer
from ..funits.branchunit import BranchUnit

class BranchUnitContainer(FUnitContainer):
    def __init__(self, numRStations, numUnits):
        super().__init__(numRStations, numUnits)

        self.branchUnits = [BranchUnit for i in range(numUnits)]
