import unittest
from components.registers import *

class RegistersCase(unittest.TestCase):
    def test_something(self):
        gpr = GPR()
        self.assertEqual(type(gpr.values[0]), int)

