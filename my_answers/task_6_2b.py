#!/usr/bin/env python3
ip = input("Введіть IP адресу: ")
ip_list = ip.split(".")
pass_correct = False
i = 0
while pass_correct == False:
    for octet in ip_list:
       try:
          (int(octet))/2
       except (ValueError, TypeError):
          ip = input("Неправильна IP адреса, введіть ще: ")
          ip_list = ip.split(".")
          i = 0
          break
       if (int(octet) < 0 or int(octet) > 255):
          ip = input("Неправильна IP адреса, введіть ще: ")
          ip_list = ip.split(".")
          i = 0
          break
       else:
          i = i + 1
          if i == 3:
              pass_correct = True

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
