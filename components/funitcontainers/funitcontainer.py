from ..rstation import RStation
from logger import log

class FUnitContainer(object):
    def __init__(self, configuration, machine):
        self.machine = machine
        self.execTime = configuration['execTime']
        self.numRStations = configuration['rStations']
        self.numUnits = configuration['numUnits']
        self.instructions = configuration['instructions']
        self.rStations = [RStation(configuration['name'] + str(i), self)
                          for i in range(self.numRStations)]

    def issue(self, instr):
        if instr.strOpcode not in self.instructions:
            return False
        if not self.hasOpenRStation():
            return False
        self.getOpenRStation().issue(instr)
        return True

    def getOpenRStation(self):
        for rStation in self.rStations:
            if not rStation.busy:
                return rStation

    def hasOpenRStation(self):
        for rStation in self.rStations:
            if not rStation.busy:
                return True
        return False

    def writeToRStation(self, rstation, value):
        pass

    def dumpRStations(self):
        return '\n'.join([station.toString() for station in self.rStations])

    def hasInstruction(self):
        anyBusy = False
        for rStation in self.rStations:
            if rStation.busy:
                anyBusy = True
        return anyBusy
