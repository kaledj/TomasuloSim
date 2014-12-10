from .funitcontainer import FUnitContainer
from ..funits.intunit import IntUnit

class IntUnitContainer(FUnitContainer):
    def __init__(self, configuration, machine):
        super().__init__(configuration, machine)
        self.intUnits = [IntUnit() for i in range(self.numUnits)]

