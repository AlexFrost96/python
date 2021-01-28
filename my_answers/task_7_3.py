#!/usr/bin/env python3
with open('CAM_table.txt') as f:
        for line in f:
            str_list = line.split()
            for arg in str_list:
                if arg =='DYNAMIC':
                    str_list.remove('DYNAMIC')
                    print(f'''{str_list[0]:<7} {str_list[1]:<17} {str_list[2]:<8}''')
                else:
                    continue
                
                       

