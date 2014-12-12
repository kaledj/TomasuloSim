from .funitcontainer import FUnitContainer
from ..funits.memunit import MemUnit
from queue import Queue
from logger import log

class MemUnitContainer(FUnitContainer):
    def __init__(self, configuration, machine):
        super().__init__(configuration, machine)
        self.funits = [MemUnit(machine) for i in range(self.numUnits)]
        self.memoryQueue = Queue()

    def issue(self, instr):
        if instr.strOpcode not in self.instructions:
            return False
        if not self.hasOpenRStation():
            return False
        rStation = self.getOpenRStation()
        self.memoryQueue.put(rStation)
        # Issuing
        rStation.instruction = instr
        rStation.busy = True
        rStation.opcode = instr.strOpcode
        rStation.execTime = self.execTime
        # Load or store
        gpr = self.machine.gprFile
        fpr = self.machine.fprFile
        rFile = gpr if instr.srcRegType == 'g' else fpr
        if rFile.status[instr.s1Reg] is not None:
            rStation.Qj = rFile.status[instr.s1Reg]
        else:
            rStation.Vj = rFile.values[instr.s1Reg]
            rStation.Qj = None
        rStation.A = instr.immediate
        rFile = gpr if instr.dstRegType == 'g' else fpr
        # Load only
        if instr.strOpcode in ['lw', 'lf']:
             rFile.status[instr.dstReg] = rStation.name
        # Store only
        if instr.strOpcode in ['sw', 'sf']:
            if rFile.status[instr.dstReg] is not None:
                rStation.Qk = rFile.status[instr.dstReg]
            else:
                rStation.Vk = rFile.values[instr.dstReg]
                rStation.Qk = None
        return True

    def execute(self):
        if not self.memoryQueue.qsize(): return
        nextMemAccess = self.memoryQueue.queue[0]
        if nextMemAccess.readyToExecute():
            log('{0} beginning execution.'.format(nextMemAccess.name))
            nextMemAccess.beginExecution()
        elif nextMemAccess.executing and nextMemAccess.execTime > 0:
            nextMemAccess.decreaseExecTime()
            log('{0} continuing execution. Time left: {1}'.format(nextMemAccess.name, nextMemAccess.execTime))
        elif nextMemAccess.execTime == 0 and not nextMemAccess.resultReady:
            log('{0} completing execution.'.format(nextMemAccess.name))
            nextMemAccess.computeResult()
            _ = self.memoryQueue.get()

    def write(self):
        for rStation in self.rStations:
            if rStation.opcode in ['sf', 'sw'] and rStation.resultReady:
                ea = rStation.result
                data = rStation.Vk
                self.machine.memory.storeWord(ea, data)
                rStation.resultWritten = True
        for rStation in self.rStations:
            cdb = rStation.write()
            if cdb:
                return cdb