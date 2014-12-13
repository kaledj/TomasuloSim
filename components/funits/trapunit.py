"""
Trap Unit

Contains trap execution unit logic.
"""

import tools
from .funit import FUnit
from logger import log
import struct


class TrapUnit(FUnit):
    """
    TrapUnit.

    A functional unit (FUnit) for executing trap instructions.
    """
    def mapFunctions(self):
        self.functions['trap'] = self._trap

    def execute(self, **kwargs):
        opcode = kwargs['opcode']
        log('{0} executed.'.format(opcode))
        self.functions[opcode](**kwargs)

    def _trap(self, **kwargs):
        """
        Implements the trap instruction.

        :param kwargs: Expecting funCode and src1 from instruction.
        :return: None
        """
        func = kwargs['funCode']
        srcVal = kwargs['src1']
        if func == 1:
            if srcVal >> 31 == 1:
                srcVal = tools.twosComp(srcVal, 32)
            print(srcVal, end="", flush=True)
        elif func == 2:
            srcVal = struct.unpack('>f', struct.pack('>I', srcVal))[0]
            print(round(srcVal, 2), end="")
        elif func == 3:
            string = self.machine.memory.readString(srcVal)
            print(string, end="")


