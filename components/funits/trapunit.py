from .funit import FUnit
from logger import log

class TrapUnit(FUnit):
    def __init__(self, machine):
        super(TrapUnit, self).__init__()
        self.machine = machine
        self.functions = {}
        self.mapFunctions()

    def mapFunctions(self):
        self.functions['trap'] = self._trap

    def execute(self, **kwargs):
        opcode = kwargs['opcode']
        log('{0} executed.'.format(opcode))
        self.functions[opcode](**kwargs)

    def _trap(self, **kwargs):
        func = kwargs['funCode']
        srcVal = kwargs['src1']
        if func == 0:
            self.machine.halted = True
        elif func in [1, 2]:
            print(srcVal, end="")
        elif func == 3:
            string = self.machine.memory.readString(srcVal)
            print(string, end="")


