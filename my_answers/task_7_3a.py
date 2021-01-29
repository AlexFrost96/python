#!/usr/bin/env python3
str_final = []
with open('CAM_table.txt') as f:
        for line in f:
            str_list = line.split()
            for arg in str_list:
                if arg =='DYNAMIC':
                    str_list.remove('DYNAMIC')
                    str_final.append(str_list)
                else:
                    continue
        str_final.sort()

for word in str_final:
    print (f'''{word[0]:<7}{word[1]:<17}{word[2]:<8}''')

                
                       

