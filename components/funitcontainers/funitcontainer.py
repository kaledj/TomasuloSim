"""
Functional Unit container.

The default container class for execution units and associated reservation
stations. Coordinates functional units and reservations statios.

Provides deafault and often sufficient default functionality.
"""

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
        self.funits = []

    def issue(self, instr):
        if instr.strOpcode not in self.instructions:
            return False
        if not self.hasOpenRStation():
            return False
        self.getOpenRStation().issue(instr)
        return True

    def execute(self):
        for rStation in self.rStations:
            rStation.execute()

    def write(self):
        for rStation in self.rStations:
            cdb = rStation.write()
            if cdb:
                return cdb

    def getOpenRStation(self):
        for rStation in self.rStations:
            if not rStation.busy:
                return rStation

    def getOpenFUnit(self):
        for unit in self.funits:
            if not unit.busy:
                return unit

    def hasOpenRStation(self):
        for rStation in self.rStations:
            if not rStation.busy:
                return True
        return False

    def hasOpenFUnit(self):
        for unit in self.funits:
            if not unit.busy:
                return True
        return False

    def updateRStations(self, cdb):
        for rStation in self.rStations:
            rStation.recieveOperands(cdb)

    def dumpRStations(self):
        return '\n'.join([station.toString() for station in self.rStations])

    def hasInstruction(self):
        anyBusy = False
        for rStation in self.rStations:
            if rStation.busy:
                anyBusy = True
        return anyBusy

    def clearRStations(self):
        for rStation in self.rStations:
            rStation.clearIfWritten()

    def getExecutingRStations(self):
        for rStation in self.rStations:
            if rStation.executing:
                yield rStation
