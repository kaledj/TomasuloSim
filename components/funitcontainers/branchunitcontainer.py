from .funitcontainer import FUnitContainer
from ..funits.branchunit import BranchUnit

class BranchUnitContainer(FUnitContainer):
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
                rStation.resultWritten = True
        for rStation in self.rStations:
            cdb = rStation.write()
            if cdb:
                return cdb