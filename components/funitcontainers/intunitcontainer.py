from .funitcontainer import FUnitContainer
from ..funits.intunit import IntUnit

class IntUnitContainer(FUnitContainer):
    def __init__(self, numRStations, numUnits):
        super().__init__(numRStations, numUnits)

        self.intUnits = [IntUnit for i in range(numUnits)]
