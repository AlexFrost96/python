#!/usr/bin/env python3
atribute = ["Prefix",
            "AD/Metric",
            "Next-Hop",
            "Last update",
            "Outbound Interface"]
with open('ospf.txt', 'r') as f:
    for line in f:
        line_list = line.replace(',','').split()
        line_list.remove("via")
        line_list.remove("O")
        print(f'''
        {atribute[0]:<20} {line_list[0]:<8}
        {atribute[1]:<20} {line_list[1]:<8}
        {atribute[2]:<20} {line_list[2]:<8}
        {atribute[3]:<20} {line_list[3]:<8}
        {atribute[4]:<20} Interface{line_list[4]:<8}''')
