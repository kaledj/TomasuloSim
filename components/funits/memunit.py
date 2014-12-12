from .funit import FUnit
from logger import log

class MemUnit(FUnit):
    def mapFunctions(self):
        self.functions['lw'] = self._lw
        self.functions['lf'] = self._lf
        self.functions['sw'] = self._sw
        self.functions['sf'] = self._sf

    def _lw(self, **kwargs):
        base = kwargs['src1']
        offset = kwargs['immediate']
        return self.machine.memory.readWord(base + offset)

    def _lf(self, **kwargs):
        base = kwargs['src1']
        offset = kwargs['immediate']
        return self.machine.memory.readWord(base + offset)

    def _sw(self, **kwargs):
        base = kwargs['src1']
        offset = kwargs['immediate']
        return base + offset

    def _sf(self, **kwargs):
        base = kwargs['src1']
        offset = kwargs['immediate']
        return base + offset