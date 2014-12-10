from .funitcontainer import FUnitContainer
from ..funits.fpunit import FPUnit

class FPUnitContainer(FUnitContainer):
    def __init__(self, configuration, machine):
        super().__init__(configuration, machine)
        self.fpUnits = [FPUnit() for i in range(self.numUnits)]
