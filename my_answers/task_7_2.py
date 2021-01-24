#!/usr/bin/env python3
filename = input('Введіть назву файлу:')
with open(filename) as f:
        for line in f:
            line_letter = line.split()
            if line.rstrip() == False:
                continue
            elif  line_letter[0] != '!':
                print(line.rstrip())
            else:
                continue
            
                
