from .funitcontainer import FUnitContainer
from ..funits.fpunit import FPUnit

class FPUnitContainer(FUnitContainer):
    def __init__(self, numRStations, numUnits):
        super().__init__(numRStations, numUnits)

        self.fpUnits = [FPUnit for i in range(numUnits)]
