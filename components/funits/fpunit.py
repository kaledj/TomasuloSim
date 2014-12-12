from .funit import FUnit
from tools import twosComp, bitLen, bitsAsFloat, floatAsBits
import struct

class FPUnit(FUnit):
    def mapFunctions(self):
        self.functions['addf'] = self._addf
        self.functions['subf'] = self._subf
        self.functions['multf'] = self._multf
        self.functions['divf'] = self._divf
        self.functions['mult'] = self._mult
        self.functions['div'] = self._div
        self.functions['cvtf2i'] = self._cvtf2i
        self.functions['cvti2f'] = self._cvti2f

    def _addf(self, **kwargs):
        src1 = kwargs['src1']
        src2 = kwargs['src2']
        result = bitsAsFloat(src1) + bitsAsFloat(src2)
        return floatAsBits(result)

    def _subf(self, **kwargs):
        src1 = kwargs['src1']
        src2 = kwargs['src2']
        result = bitsAsFloat(src1) - bitsAsFloat(src2)
        return floatAsBits(result)

    def _multf(self, **kwargs):
        src1 = kwargs['src1']
        src2 = kwargs['src2']
        result = bitsAsFloat(src1) * bitsAsFloat(src2)
        return floatAsBits(result)

    def _divf(self, **kwargs):
        src1 = kwargs['src1']
        src2 = kwargs['src2']
        result = bitsAsFloat(src1) / bitsAsFloat(src2)
        return floatAsBits(result)

    def _mult(self, **kwargs):
        return kwargs['src1'] * kwargs['src2']

    def _div(self, **kwargs):
        return int(kwargs['src1'] / kwargs['src2'])

    def _cvtf2i(self, **kwargs):
        src1 = kwargs['src1']
        return int(bitsAsFloat(src1))

    def _cvti2f(self, **kwargs):
        src1 = kwargs['src1']
        src1 = struct.unpack('>i', struct.pack('>I',src1))[0]
        src1 = float(src1)
        result = struct.unpack('>I', struct.pack('>f',src1))[0]
        return result
