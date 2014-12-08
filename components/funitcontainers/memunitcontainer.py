from .funitcontainer import FUnitContainer
from ..funits.memunit import MemUnit

class MemUnitContainer(FUnitContainer):
    def __init__(self, numRStations, numUnits):
        super().__init__(numRStations, numUnits)

        self.memUnits = [MemUnit for i in range(numUnits)]
