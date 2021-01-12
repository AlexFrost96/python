#!/usr/bin/env python3

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

input1 = input("Введіть ім'я пристрою " + str(list(london_co)) + ": ")
list_of_in1 = str(list(london_co[input1])).replace("'",'')
input2 = input("Введіть ім'я параметру " + list_of_in1 + ": ")
london2 = london_co[input1].copy() 

print (london2.get(input2, "Такого параметру немає у списку"))
