#!/usr/bin/env python3
mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
mac_cisco_list = []
for mac_bad in mac :
	mac_cisco = ""
	for letter in mac_bad :
		if letter == ":":
			letter = "."
			mac_cisco = mac_cisco + letter
		else:
			mac_cisco = mac_cisco + letter
	mac_cisco_list.append(mac_cisco)
	print(mac_cisco)
