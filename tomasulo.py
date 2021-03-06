"""
Tomasulo main module.

"""
import argparse
import logger
from machine import Machine


def main():
    """
    Main entry point.
    Parses command line argument and begins execution.

    :return: None
    """
    parser = argparse.ArgumentParser(description='Simulate execution of DLX code on a Tomasulo processor.')
    parser.add_argument('-f', type=str, dest='filename', required=True, help='The input file. Must be a .hex file.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity.')
    args = parser.parse_args()

    logger.setLogLevel(1 if args.verbose else 0)

    # Run
    machine = Machine()
    machine.loadProgram(args.filename)
    machine.run()

if __name__ == '__main__':
    main()
