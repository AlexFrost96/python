#!/usr/bin/env python3
filename = input('Введіть назву файлу:')
ignore = ["duplex", "alias", "Current configuration"]
with open(filename) as f:
        for line in f:
            if   line.startswith(ignore[0]) or line.startswith(ignore[1]) or line.startswith(ignore[2]):
                continue
            else:
                k = open('config_sw1_cleared.txt', 'a')
                k.write(line + '\n') 
                k.close()
                       

