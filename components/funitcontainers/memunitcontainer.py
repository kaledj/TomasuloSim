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
        rStation.issue(instr)
        self.memoryQueue.put(rStation)
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
        stored = False
        for rStation in self.rStations:
            if not stored and rStation.opcode in ['sf', 'sw'] and rStation.resultReady:
                ea = rStation.result
                data = rStation.Vk
                self.machine.memory.storeWord(ea, data)
                rStation.resultWritten = True
                stored = True
        for rStation in self.rStations:
            cdb = rStation.write()
            if cdb:
                return cdb