from .funitcontainer import FUnitContainer
from ..funits.memunit import MemUnit

class MemUnitContainer(FUnitContainer):
    def __init__(self, configuration, machine):
        super().__init__(configuration, machine)
        self.memUnits = [MemUnit() for i in range(self.numUnits)]
