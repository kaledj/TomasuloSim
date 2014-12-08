from ..rstation import RStation
from logger import log

class FUnitContainer(object):
    def __init__(self, numRStations, numUnits):
        self.numRStations = numRStations
        self.numUnits = numUnits

        self.rStations = [RStation(i) for i in range(self.numRStations)]

    def hasOpenRStation(self):
        pass

    def writeToRStation(self, rstation, value):
        pass

    def dumpRStations(self):
        return '\n'.join([station.dump() for station in self.rStations])
