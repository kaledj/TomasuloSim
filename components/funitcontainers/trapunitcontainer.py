from .funitcontainer import FUnitContainer
from ..funits.trapunit import TrapUnit

class TrapUnitContainer(FUnitContainer):
    def __init__(self, numRStations, numUnits):
        super().__init__(numRStations, numUnits)

        self.trapUnits = [TrapUnit for i in range(numUnits)]


