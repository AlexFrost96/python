#!/usr/bin/env python3
access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]
access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del","17"],"0/777": ["only", "5555", "4444"]}
for intf, vlan in access.items(): 
    print("interface FastEthernet" + intf) 
    for command in access_template:
        if command.endswith("access vlan"): 
            print(f" {command} {vlan}")
        else:
            print(f" {command}")
for intf, vlan in trunk.items():
    print("interface GigabitEthernet" + intf)
    i = 0
    for command in trunk_template:
        if  vlan[0] == "add" and i == 2:
            vlan.remove('add')
            vlan_str = ','.join(vlan)
            
            print(f" {command}" + " add " + vlan_str)
        elif vlan[0] == "only" and i == 2:
            vlan.remove('only')
            vlan_str = ','.join(vlan)
            
            print(f" {command} " + vlan_str)
        elif vlan[0] == "del" and i == 2:
            vlan.remove('del')
            vlan_str = ','.join(vlan)
            
            print(f" {command}" + " remove " + vlan_str)
        else:
            print(f" {command}")
            i = i + 1


        
