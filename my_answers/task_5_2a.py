#!/usr/bin/env python3
input1 = input("Введіть ip адресу: ").split("/")
ip = input1[0].split(".")
ip_bin_first_octet = (8 - len(bin(int(ip[0])).replace("0b",'')))*"0"+ bin(int(ip[0])).replace("0b",'')
ip_bin_second_octet = (8 - len(bin(int(ip[1])).replace("0b",'')))*"0"+ bin(int(ip[1])).replace("0b",'')
ip_bin_third_octet = (8 - len(bin(int(ip[2])).replace("0b",'')))*"0"+ bin(int(ip[2])).replace("0b",'')
ip_bin_fourth_octet = (8 - len(bin(int(ip[3])).replace("0b",'')))*"0"+ bin(int(ip[3])).replace("0b",'')
ip_bin =ip_bin_first_octet + ip_bin_second_octet + ip_bin_third_octet + ip_bin_fourth_octet
host_space = 32 - int(input1[1])
ip_bin_mask = ip_bin[0:int(input1[1])] + "0"*host_space
mask = "1"*int(input1[1]) + "0"*host_space
first_octet = int(mask[0])*128 + int(mask[1])*64 + int(mask[2])*32 + int(mask[3])*16 + int(mask[4])*8 + int(mask[5])*4 + int(mask[6])*2 + int(mask[7])*1
second_octet = int(mask[8])*128 + int(mask[9])*64 + int(mask[10])*32 + int(mask[11])*16 + int(mask[12])*8 + int(mask[13])*4 + int(mask[14])*2 + int(mask[15])*1
third_octet = int(mask[16])*128 + int(mask[17])*64 + int(mask[18])*32 + int(mask[19])*16 + int(mask[20])*8 + int(mask[21])*4 + int(mask[22])*2 + int(mask[23])*1
fourth_octet = int(mask[24])*128 + int(mask[25])*64 + int(mask[26])*32 + int(mask[27])*16 + int(mask[28])*8 + int(mask[29])*4 + int(mask[30])*2 + int(mask[31])*1
print(f'''
Network:
{ip[0]:<8} {ip[1]:<8} {ip[2]:<8} {ip[3]:<8} 
{ip_bin_mask[0:7]:<8} {ip_bin_mask[8:15]:<8} {ip_bin_mask[16:23]:<8} {ip_bin_mask[24:31]:<8}''')
print(f'''
Mask:
/{input1[1]}
{first_octet:<8} {second_octet:<8} {third_octet:<8} {fourth_octet:<8}
{mask[0:7]:<8} {mask[8:15]:<8} {mask[16:23]:<8} {mask[24:31]:<8} ''')

