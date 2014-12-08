"""
Logger

Controls the level of program output.
"""
LOGLEVEL = 0

def setLogLevel(logLevel):
    global LOGLEVEL
    LOGLEVEL = logLevel

def log(string):
    if LOGLEVEL:
        print(string)
