#!/usr/bin/env python3
ip = input("Введіть IP адресу: ")
ip_list = ip.split(".")
for octet in ip_list:
    try:
        (int(octet))/2
    except (ValueError, TypeError):
        octet = "bad"
        break
    if (int(octet) < 0 or int(octet) > 255):
        octet = "bad"
        break
if octet == "bad":
    print("Неправильна IP адреса")
elif int(ip_list[0]) > 0 and int(ip_list[0]) < 224:
    print("Це unicast адреса")
elif int(ip_list[0]) > 223 and int(ip_list[0]) < 240:
    print("Це multicast адреса")
elif ip == "255.255.255.255" :
    print("Це broadcast адреса")
elif ip == "0.0.0.0":
    print("Це unassigned адреса")
else :
    print("Це unused адреса")


