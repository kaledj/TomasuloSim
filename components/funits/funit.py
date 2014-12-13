"""
Functional unit.

This module contains basic shared functionality between all functional units.

Provides a common and generic execution functionality that dispatches the
correct operation.
"""

from logger import log


class FUnit(object):
    """
    FUnit class.

    The base class of all functional units.
    """
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