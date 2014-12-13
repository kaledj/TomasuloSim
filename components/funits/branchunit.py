"""
Branch Unit.

Contains execution logic for a branch function unit.
"""

from .funit import FUnit


class BranchUnit(FUnit):
    """
    BranchUnit class.

     A functional unit for executing branch instructions.
    """
    def mapFunctions(self):
        self.functions['beqz'] = self._beqz
        self.functions['j'] = self._j
        self.functions['jr'] = self._jr
        self.functions['jal'] = self._jal
        self.functions['jalr'] = self._jalr

    def _beqz(self, **kwargs):
        src1 = kwargs['src1']
        imm = kwargs['name']
        if src1 == 0:
            return self.machine.PC + 4 + imm
        else:
            return self.machine.PC + 4

    def _j(self, **kwargs):
        name = kwargs['name']
        return self.machine.PC + name + 4

    def _jr(self, **kwargs):
        src1 = kwargs['src1']
        return src1

    def _jal(self, **kwargs):
        name = kwargs['name']
        return self.machine.PC + 4 + name

    def _jalr(self, **kwargs):
        src1 = kwargs['src1']
        return src1

