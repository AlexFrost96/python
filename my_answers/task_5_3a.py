#!/usr/bin/env python3

access_template = [
"switchport mode access", "switchport access vlan {}",
"switchport nonegotiate", "spanning-tree portfast",
"spanning-tree bpduguard enable"
]

trunk_template = [
"switchport trunk encapsulation dot1q", "switchport mode trunk",
"switchport trunk allowed vlan {}"
]
print_int = { "access": "Введіть номер VLAN: ", "trunk": "Введіть дозволені VLAN: "}

input_mode = input('Введіть режим роботи порта (access/trunk): ')
input_int = input('Введіть тип та номер інтерфейсу: ')
input_vlans = input(print_int[input_mode])
access_template.insert(0,'interface ' + input_int)
trunk_template.insert(0,'interface ' + input_int)

london = { "access" :
          '''
	  interface {}
          switchport mode access
          switchport access vlan {}
          switchport nonegotiate
          spanning-tree portfast
          spanning-tree bpduguard enable
          ''', 
          "trunk" :
	  '''
	  interface {}
	  switchport trunk encapsulation dot1q
          switchport mode trunk
	  switchport trunk allowed vlan {}
          '''

     }

print(london[input_mode].format(input_int,input_vlans))

