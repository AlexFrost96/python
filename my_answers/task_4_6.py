ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_string = ospf_route.replace(',','')
ospf_split = ospf_string.split()
ospf_split.pop(2)
name_of_atribute = '''
     Prefix {:<40}
     AD/Metric {:<40}
     Next-Hop {:<40}
     Last update {:<40}
     Outbound Interface {:<40}
     '''
print(name_of_atribute.format(*ospf_split))

