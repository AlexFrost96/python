#!/usr/bin/env python3
access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]
access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}
access_template = []
def generate_access_config(intf_vlan_mapping, access_template): 
"""
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {"FastEthernet0/12": 10,
         "FastEthernet0/14": 11,
         "FastEthernet0/16": 17}
    access_template - список команд для порта в режиме access
Возвращает список всех портов в режиме access с конфигурацией на основе␣ 􏰀→шаблона
"""
    intf_vlan_mapping = access_mode_template
    access_config = access_template
    for intf in intf_vlan_mapping:
        for command in access_config:
            if command == 
        
