import unittest
from machine import Machine
import sys
import io
from contextlib import redirect_stdout
import os

class TestTomasulo(unittest.TestCase):
    # def setUp(self):
    #     # Capture output
    #     self._stdout = sys.stdout
    #     sys.stdout = self._stringIO = io.StringIO()
    #
    # def tearDown(self):
    #     # Restore output
    #     sys.stdout = self._stdout

    def test_intUnit1(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit1.hex')
        machine.run()
        with open('Tomasulo/intUnit1.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_intUnit2(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit2.hex')
        machine.run()
        with open('Tomasulo/intUnit2.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_intUnit3(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit3.hex')
        machine.run()
        with open('Tomasulo/intUnit3.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_intUnit4(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit4.hex')
        machine.run()
        with open('Tomasulo/intUnit4.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_intUnit5(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit5.hex')
        machine.run()
        with open('Tomasulo/intUnit5.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)
        
    def test_intUnit6(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit6.hex')
        machine.run()
        with open('Tomasulo/intUnit6.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)
        
    def test_intUnit7(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit7.hex')
        machine.run()
        with open('Tomasulo/intUnit7.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_intUnit8(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/intUnit8.hex')
        machine.run()
        with open('Tomasulo/intUnit8.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_allInts(self):
        for i in range(1, 9):
            sys.stdout = output = io.StringIO()
            machine = Machine()
            machine.loadProgram('Tomasulo/intUnit{0}.hex'.format(i))
            machine.run()
            with open('Tomasulo/intUnit{0}.out'.format(i), 'r') as answerFile:
                answer = answerFile.read()
            self.assertEquals(output.getvalue(), answer)

    def test_brUnit1(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/brUnit1.hex')
        machine.run()
        with open('Tomasulo/brUnit1.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_brUnit2(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/brUnit2.hex')
        machine.run()
        with open('Tomasulo/brUnit2.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_brUnit3(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/brUnit3.hex')
        machine.run()
        with open('Tomasulo/brUnit3.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_brUnit4(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/brUnit4.hex')
        machine.run()
        with open('Tomasulo/brUnit4.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_brUnit5(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/brUnit5.hex')
        machine.run()
        with open('Tomasulo/brUnit5.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_brUnit6(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/brUnit6.hex')
        machine.run()
        with open('Tomasulo/brUnit6.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_allBranches(self):
        for i in range(1, 8):
            sys.stdout = output = io.StringIO()
            machine = Machine()
            machine.loadProgram('Tomasulo/brUnit{0}.hex'.format(i))
            machine.run()
            with open('Tomasulo/brUnit{0}.out'.format(i), 'r') as answerFile:
                answer = answerFile.read()
            self.assertEquals(output.getvalue(), answer)

    def test_fpUnit1(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/fpUnit1.hex')
        machine.run()
        with open('Tomasulo/fpUnit1.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_fpUnit2(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/fpUnit2.hex')
        machine.run()
        with open('Tomasulo/fpUnit2.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_fpUnit3(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/fpUnit3.hex')
        machine.run()
        with open('Tomasulo/fpUnit3.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_fpUnit4(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/fpUnit4.hex')
        machine.run()
        with open('Tomasulo/fpUnit4.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_fpUnit5(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/fpUnit5.hex')
        machine.run()
        with open('Tomasulo/fpUnit5.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_fpUnit6(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/fpUnit6.hex')
        machine.run()
        with open('Tomasulo/fpUnit6.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_fpUnit7(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/fpUnit7.hex')
        machine.run()
        with open('Tomasulo/fpUnit7.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_fpUnit8(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/fpUnit8.hex')
        machine.run()
        with open('Tomasulo/fpUnit8.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_allFPs(self):
        for i in range(1, 8):
            sys.stdout = output = io.StringIO()
            machine = Machine()
            machine.loadProgram('Tomasulo/fpUnit{0}.hex'.format(i))
            machine.run()
            with open('Tomasulo/fpUnit{0}.out'.format(i), 'r') as answerFile:
                answer = answerFile.read()
            self.assertEquals(output.getvalue(), answer)

    def test_memUnit1(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/memUnit1.hex')
        machine.run()
        with open('Tomasulo/memUnit1.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_memUnit2(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/memUnit2.hex')
        machine.run()
        with open('Tomasulo/memUnit2.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_memUnit3(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/memUnit3.hex')
        machine.run()
        with open('Tomasulo/memUnit3.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_memUnit4(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/memUnit4.hex')
        machine.run()
        with open('Tomasulo/memUnit4.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_memUnit5(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/memUnit5.hex')
        machine.run()
        with open('Tomasulo/memUnit5.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_memUnit6(self):
        sys.stdout = output = io.StringIO()
        machine = Machine()
        machine.loadProgram('Tomasulo/memUnit6.hex')
        machine.run()
        with open('Tomasulo/memUnit6.out', 'r') as answerFile:
            answer = answerFile.read()
        self.assertEquals(output.getvalue(), answer)

    def test_allMems(self):
        for i in range(1, 8):
            sys.stdout = output = io.StringIO()
            machine = Machine()
            machine.loadProgram('Tomasulo/memUnit{0}.hex'.format(i))
            machine.run()
            with open('Tomasulo/memUnit{0}.out'.format(i), 'r') as answerFile:
                answer = answerFile.read()
            self.assertEquals(output.getvalue(), answer)

    def test_all(self):
        sys.stdout = output = io.StringIO()
        for inputFile in os.listdir('Tomasulo'):
            if inputFile.endswith('.dlx'): continue
            if inputFile.endswith('.out'): continue
            machine = Machine()
            machine.loadProgram('Tomasulo/' + inputFile)
            machine.run()
            with open('Tomasulo/' + inputFile.stip('.hex') + '.out', 'r') as answerFile:
                answer = answerFile.read()
            self.assertEquals(output.getvalue(), answer)

