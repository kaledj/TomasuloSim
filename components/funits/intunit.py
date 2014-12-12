from .funit import FUnit
from logger import log

class IntUnit(FUnit):
    def __init__(self):
        super(IntUnit, self).__init__()
        self.functions = {}
        self.mapFunctions()
        
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

    def execute(self, **kwargs):
        opcode = kwargs['opcode']
        log('{0} executed.'.format(opcode))
        return self.functions[opcode](**kwargs)
        
    def _addi(self, **kwargs):
        return kwargs['src1'] + kwargs['immediate']

    def _add(self, **kwargs):
        return kwargs['src1'] + kwargs['src2']

    def _sub(self, **kwargs):
        pass

    def _and(self, **kwargs):
        pass

    def _or(self, **kwargs):
        pass

    def _xor(self, **kwargs):
        pass

    def _movf(self, **kwargs):
        pass

    def _movfp2i(self, **kwargs):
        pass

    def _movi2fp(self, **kwargs):
        pass
