
intUnits = {'rStations': 8,
            'numUnits': 3,
            'execTime': 1,
            'instructions': ['addi', 'nop', 'add', 'sub', 'and', 'or', 'xor',
                             'movf', 'movfp2i', 'movi2fp']}

trapUnits = {'rStations': 4,
            'numUnits': 1,
            'execTime': 1,
            'instructions': ['trap']}

branchUnits = {'rStations': 1,
            'numUnits': 1,
            'execTime': 1,
            'instructions': ['beqz', 'j', 'jr', 'jal', 'jalr']}

memUnits = {'rStations': 8,
            'numUnits': 1,
            'execTime': 2,
            'instructions': ['lw', 'lf', 'sw', 'sf']}

fpUnits = {'rStations': 8,
            'numUnits': 2,
            'execTime': 4,
            'instructions': ['addf', 'subf', 'multf', 'divf', 'mult', 'div',
                             'cvtf2i', 'cvti2f']}