#!/usr/bin/env python3

ip = input("Введіть IP адресу: ")
ip_list = ip.split(".")
if int(ip_list[0]) > 0 and int(ip_list[0]) < 224:
	print("Це unicast адреса")
elif int(ip_list[0]) > 223 and int(ip_list[0]) < 240:
	print("Це multicast адреса")
elif ip == "255.255.255.255" :
	print("Це broadcast адреса")
elif ip == "0.0.0.0":
	print("Це unassigned адреса")
else :
	print("Це unused адреса")





