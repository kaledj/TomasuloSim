from logger import log

class FUnit(object):
    def __init__(self, machine):
        self.busy = False
        self.machine = machine
        self.functions = {}
        self.mapFunctions()

    def mapFunctions(self):
        pass

    def execute(self, **kwargs):
        opcode = kwargs['opcode']
        log('{0} executed.'.format(opcode))
        return self.functions[opcode](**kwargs)