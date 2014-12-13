"""
Integer Unit container.

Manages a group and integer units and associated reservation statsions.
Current default functionality does not need to be extended to provide
functionality needed.
"""

from .funitcontainer import FUnitContainer
from ..funits.intunit import IntUnit

class IntUnitContainer(FUnitContainer):
    def __init__(self, configuration, machine):
        super().__init__(configuration, machine)
        self.funits = [IntUnit(machine) for i in range(self.numUnits)]

