"""
Branch Unit container.

This module contains 1 or more branch units and associated reservation
stations. Overwrites the default issue and write logic to force stalling and
allow writing to the PC.
"""

from .funitcontainer import FUnitContainer
from ..funits.branchunit import BranchUnit

class BranchUnitContainer(FUnitContainer):
    """
    BranchUnitContainer class.

    A specific functional unit container for branches. Maintains and
    managers branch units specifically.
    """
    def __init__(self, configuration, machine):
        super().__init__(configuration, machine)
        self.funits = [BranchUnit(machine) for i in range(self.numUnits)]

    def issue(self, instr):
        if instr.strOpcode not in self.instructions:
            return False
        if not self.hasOpenRStation():
            return False
        self.getOpenRStation().issue(instr)
        return False

    def write(self):
        for rStation in self.rStations:
            if rStation.resultReady:
                self.machine.PC = rStation.result
                if rStation.opcode in ['jal', 'jalr']:
                    self.machine.gprFile.values[31] = rStation.PC + 4
                    if self.machine.gprFile.status[31] == rStation.name:
                       self.machine.gprFile.status[31] = None
                rStation.resultWritten = True
                return None