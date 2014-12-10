from .funitcontainer import FUnitContainer
from ..funits.trapunit import TrapUnit

class TrapUnitContainer(FUnitContainer):
    def __init__(self, configuration, machine):
        super().__init__(configuration, machine)
        self.trapUnits = [TrapUnit() for i in range(self.numUnits)]
