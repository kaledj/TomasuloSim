"""
Logger

Controls the level of program output. If output is not
desired, this module can act to silence it. When verbose mode is toggled,
this module will allow output though.
"""

LOGLEVEL = 0

def setLogLevel(logLevel):
    global LOGLEVEL
    LOGLEVEL = logLevel

def log(string):
    if LOGLEVEL:
        print(string)
