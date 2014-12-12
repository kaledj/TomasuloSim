from logger import log

class RStation(object):
    def __init__(self, name, container):
        self.container = container
        self.usingUnit = None
        self.execTime = None
        self.name = name
        self.busy = False
        self.executing = False
        self.instruction = None
        self.opcode = None
        self.Vj = None
        self.Vk = None
        self.Qj = None
        self.Qk = None
        self.A = None
        self.result = None
        self.resultReady = None
        self.resultWritten = None

    def toString(self):
        s = "{0} Time:{9} Busy:{1} Op:{2} Vj:{3} Vk:{4} Qj:{5} Qk:{6} A:{7} Result:{8}".format(
            self.name, self.busy, self.opcode, self.Vj, self.Vk, self.Qj,
            self.Qk, self.A, self.result, self.execTime)
        return s

    def write(self):
        if self.resultReady:
            log('{0} writing its result to CDB.'.format(self.name))
            self.resultWritten = True
            return self.name, self.result

    def execute(self):
        if self.readyToExecute():
            log('{0} beginning execution.'.format(self.name))
            self.beginExecution()
        elif self.executing and self.execTime > 0:
            self.decreaseExecTime()
            log('{0} continuing execution. Time left: {1}'.format(self.name, self.execTime))
        elif self.execTime == 0 and not self.resultReady:
            log('{0} completing execution.'.format(self.name))
            self.computeResult()

    def issue(self, instr):
        self.instruction = instr
        self.busy = True
        self.opcode = instr.strOpcode
        self.execTime = self.container.execTime
        self.storeOperands(instr)
        if instr.dstReg is not None:
            if instr.regType == 'fpr':
                registerFile = self.container.machine.fprFile
            else:
                registerFile = self.container.machine.gprFile
            registerFile.status[instr.dstReg] = self.name
        log("{0} issued to {1}".format(instr.strOpcode, self.name))

    def decreaseExecTime(self):
        self.execTime -= 1 if self.execTime > 0 else 0

    def clearIfWritten(self):
        if self.resultWritten:
            self.clear()

    def storeOperands(self, instr):
        src1 = instr.s1Reg
        src2 = instr.s2Reg
        imm = instr.immediate
        if instr.regType == 'fpr':
            registerFile = self.container.machine.fprFile
        else:
            registerFile = self.container.machine.gprFile
        if src1 is not None:
            if registerFile.status[src1] is not None:
                self.Qj = registerFile.status[src1]
            else:
                self.Vj = registerFile.values[src1]
        if src2 is not None:
            if registerFile.status[src2] is not None:
                self.Qk = registerFile.status[src2]
            else:
                self.Vk = registerFile.values[src2]
        if imm is not None:
            self.A = imm

    def recieveOperands(self, cdb):
        if cdb is not None:
            source, value = cdb
            if self.Qj == source:
                self.Vj = value
                self.Qj = None
            if self.Qk == source:
                self.Vk = value
                self.Qk = None

    def computeResult(self):
        self.result = self.usingUnit.execute(**self.getExecutionArgs())
        self.resultReady = True
        self.executing = False
        self.usingUnit.busy = False
        self.usingUnit = None

    def beginExecution(self):
        self.decreaseExecTime()
        self.usingUnit = self.container.getOpenFUnit()
        self.usingUnit.busy = True
        self.executing = True
        self.resultWritten = False
        self.resultReady = False

    def hasOperands(self):
        return self.Qj is None and self.Qk is None

    def readyToExecute(self):
        a = self.hasOperands()
        b = self.container.hasOpenFUnit()
        c = not self.executing
        d = self.busy
        e = not self.resultReady
        return a and b and c and d and e

    def clear(self):
        self.execTime = None
        self.busy = False
        self.opcode = None
        self.Vj = None
        self.Vk = None
        self.Qj = None
        self.Qk = None
        self.A = None
        self.result = None
        self.resultReady = None
        self.resultWritten = None

    def getExecutionArgs(self):
        return {'opcode': self.opcode,
                'src1': self.Vj,
                'src2': self.Vk,
                's1Reg': self.instruction.s1Reg,
                'immediate': self.A,
                'funCode': self.instruction.funCode
        }
