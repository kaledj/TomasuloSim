import tools
from .funit import FUnit
from logger import log

class TrapUnit(FUnit):
    def mapFunctions(self):
        self.functions['trap'] = self._trap

    def execute(self, **kwargs):
        opcode = kwargs['opcode']
        log('{0} executed.'.format(opcode))
        self.functions[opcode](**kwargs)

    def _trap(self, **kwargs):
        func = kwargs['funCode']
        srcVal = kwargs['src1']
        # if func == 0:
        if func == 1:
            print(srcVal, end="")
        elif func == 2:
            srcVal = tools.bitsAsFloat(srcVal)
            print(round(srcVal, 2), end="")
        elif func == 3:
            string = self.machine.memory.readString(srcVal)
            print(string, end="")


