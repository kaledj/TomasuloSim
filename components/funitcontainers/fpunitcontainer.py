"""
Floating Point container

This module contains logic for managing a group of floating point
execution units and associated reservations stations. Default logic
currently handles most FP uses so this module simply allow for future expansion.
"""

from .funitcontainer import FUnitContainer
from ..funits.fpunit import FPUnit

class FPUnitContainer(FUnitContainer):
    def __init__(self, configuration, machine):
        super().__init__(configuration, machine)
        self.funits = [FPUnit(machine) for i in range(self.numUnits)]
