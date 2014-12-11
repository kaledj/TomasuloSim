
intUnits = {'name': 'IntRS',
            'rStations': 8,
            'numUnits': 3,
            'execTime': 1,
            'instructions': ['addi', 'nop', 'add', 'sub', 'and', 'or', 'xor',
                             'movf', 'movfp2i', 'movi2fp']}

trapUnits = {'name': 'TrapRS',
            'rStations': 4,
            'numUnits': 1,
            'execTime': 1,
            'instructions': ['trap']}

branchUnits = {'name': 'BranchRS',
            'rStations': 1,
            'numUnits': 1,
            'execTime': 1,
            'instructions': ['beqz', 'j', 'jr', 'jal', 'jalr']}

memUnits = {'name': 'MemRS',
            'rStations': 8,
            'numUnits': 1,
            'execTime': 2,
            'instructions': ['lw', 'lf', 'sw', 'sf']}

fpUnits = {'name': 'FPRS',
            'rStations': 8,
            'numUnits': 2,
            'execTime': 4,
            'instructions': ['addf', 'subf', 'multf', 'divf', 'mult', 'div',
                             'cvtf2i', 'cvti2f']}