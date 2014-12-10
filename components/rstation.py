


class RStation(object):
    def __init__(self, name, container):
        self.container = container
        self.execTime = None
        self.name = name
        self.busy = None
        self.opcode = None
        self.Vj = None
        self.Vk = None
        self.Qj = None
        self.Qk = None
        self.A = None
        self.result = None
        self.resutReady = None
        self.resultWritten = None

    def toString(self):
        s = "{0} Busy:{1} Op:{2} Vj:{3} Vk:{4} Qj:{5} Qk:{6} A:{7}".format(
            self.name, self.busy, self.opcode, self.Vj, self.Vk, self.Qj,
            self.Qk, self.A)
        return s

    def issue(self, instr):
        self.busy = True
        self.execTime = self.container.execTime
        self.opcode = instr.strOpcode
        self.storeOperands(instr)

    def decreaseExecTime(self):
        self.execTime -= 1

    def clear(self):
        self.execTime = None
        self.busy = None
        self.opcode = None
        self.Vj = None
        self.Vk = None
        self.Qj = None
        self.Qk = None
        self.A = None
        self.result = None
        self.resutReady = None
        self.resultWritten = None

    def storeOperands(self, instr):
        src1 = instr.s1Reg
        src2 = instr.s2Reg
        imm = instr.immediate
        if instr.regType == 'fpr':
            registerFile = self.container.machine.fprFile
        else:
            registerFile = self.container.machine.gprFile
        if src1 is not None:
            self.Vj = registerFile.values[src1]
            self.Qj = registerFile.status[src1]
        if src2 is not None:
            self.Vk = registerFile.values[src2]
            self.Qk = registerFile.status[src2]
        if imm is not None:
            self.A = imm

    def isBusy(self):
        return self.busy