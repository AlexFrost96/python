#!/usr/bin/env python3
filename = input('Введіть назву файлу:')
ignore = ["duplex", "alias", "Current configuration"]
with open(filename) as f:
        for line in f:
            if  line.startswith('!') == False and line.startswith(ignore[0]) == False and line.startswith(ignore[1]) == False and line.startswith(ignore[2]) == False:
                print(line.rstrip())
            else:
                continue
            

