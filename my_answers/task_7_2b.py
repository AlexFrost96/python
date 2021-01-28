#!/usr/bin/env python3
filename = input('Введіть назву файлу:')
input_save = input('Введіть назву файлу куди зберегти:')
ignore = ["duplex", "alias", "Current configuration"]
with open(filename) as f:
        for line in f:
            if   line.startswith(ignore[0]) or line.startswith(ignore[1]) or line.startswith(ignore[2]):
                continue
            else:
                k = open(input_save, 'a')
                k.write(line + '\n') 
                k.close()
                       

