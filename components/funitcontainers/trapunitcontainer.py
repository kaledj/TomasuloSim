from .funitcontainer import FUnitContainer
from ..funits.trapunit import TrapUnit
from queue import Queue
from logger import log

class TrapUnitContainer(FUnitContainer):
    def __init__(self, configuration, machine):
        super().__init__(configuration, machine)
        self.funits = [TrapUnit(machine) for i in range(self.numUnits)]
        self.trapQueue = Queue()
        # self.nextTrap = None

    def issue(self, instr):
        if instr.strOpcode not in self.instructions:
            return False
        if not self.hasOpenRStation():
            return False
        rStation = self.getOpenRStation()
        rStation.issue(instr)
        self.trapQueue.put(rStation)
        return True

    def execute(self):
        if not self.trapQueue.qsize(): return
        nextTrap = self.trapQueue.queue[0]
        if nextTrap.readyToExecute():
            log('{0} beginning execution.'.format(nextTrap.name))
            nextTrap.beginExecution()
        elif nextTrap.executing and nextTrap.execTime > 0:
            nextTrap.decreaseExecTime()
            log('{0} continuing execution. Time left: {1}'.format(nextTrap.name, nextTrap.execTime))
        elif nextTrap.execTime == 0 and not nextTrap.resultReady:
            log('{0} completing execution.'.format(nextTrap.name))
            nextTrap.computeResult()
            _ = self.trapQueue.get()
