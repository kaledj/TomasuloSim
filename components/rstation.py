
class RStation(object):
    def __init__(self, name):
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

    def dump(self):
        return str(self.name)

