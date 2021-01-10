config = "switchport trunk allowed vlan 1,3,10,20,30,100"
list_of_vlan = list(config.strip('switchport trunk allowed vlan').split(','))
print(list_of_vlan)
