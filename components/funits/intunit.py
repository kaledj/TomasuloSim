import tools
from .funit import FUnit
from logger import log

class IntUnit(FUnit):
    # def __init__(self):
    #     super(IntUnit, self).__init__()
    #     self.functions = {}
    #     self.mapFunctions()
        
    def mapFunctions(self):
        self.functions['addi'] = self._addi
        self.functions['add'] = self._add
        self.functions['sub'] = self._sub
        self.functions['and'] = self._and
        self.functions['or'] = self._or
        self.functions['xor'] = self._xor
        self.functions['movf'] = self._movf
        self.functions['movfp2i'] = self._movfp2i
        self.functions['movi2fp'] = self._movi2fp
        self.functions['nop'] = self._nop

    def _addi(self, **kwargs):
        src1 = kwargs['src1']
        if src1 >> 31 == 1:
                src1 = tools.twosComp(src1, 32)
        return src1 + kwargs['immediate']

    def _add(self, **kwargs):
        return kwargs['src1'] + kwargs['src2']

    def _sub(self, **kwargs):
        return kwargs['src1'] - kwargs['src2']

    def _and(self, **kwargs):
        return kwargs['src1'] & kwargs['src2']

    def _or(self, **kwargs):
        return kwargs['src1'] | kwargs['src2']

    def _xor(self, **kwargs):
        return kwargs['src1'] ^ kwargs['src2']

    def _movf(self, **kwargs):
        return kwargs['src1']

    def _movfp2i(self, **kwargs):
        return kwargs['src1']

    def _movi2fp(self, **kwargs):
        return kwargs['src1']

    def _nop(self, **kwargs):
        return None