#!/usr/bin/env python3
filename = input('Введіть назву файлу:')

with open(filename) as f:
        for line in f:
            if  line.startswith('!') == False:
                print(line.rstrip())
            else:
                continue
            
                
