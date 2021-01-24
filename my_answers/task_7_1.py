#!/usr/bin/env python3
with open('ospf.txt', 'r') as f:
    for line in f:
        line_list = line.replace(',','').split()
        line_list.remove("via")
        line_list.remove("O")
        print(f'''
        Prefix {line_list[0]:<8}
        AD/Metric {line_list[1]:<8}
        Next-Hop {line_list[2]:<8}
        Last update {line_list[3]:<8}
        Outbound Interface{line_list[4]:<8}''')
