#!/usr/bin/env python3
input1 = input("Введіть ip адресу: ").split("/")
ip = input1[0].split(".")
ip_bin_first_octet = (8 - len(bin(int(ip[0])).replace("0b",'')))*"0"+ bin(int(ip[0])).replace("0b",'')
ip_bin_second_octet = (8 - len(bin(int(ip[1])).replace("0b",'')))*"0"+ bin(int(ip[1])).replace("0b",'')
ip_bin_third_octet = (8 - len(bin(int(ip[2])).replace("0b",'')))*"0"+ bin(int(ip[2])).replace("0b",'')
ip_bin_fourth_octet = (8 - len(bin(int(ip[3])).replace("0b",'')))*"0"+ bin(int(ip[3])).replace("0b",'')
ip_bin =ip_bin_first_octet + ip_bin_second_octet + ip_bin_third_octet + ip_bin_fourth_octet
host_space = 32 - int(input1[1])
range = int(input1[1]) + 1
ip_bin_mask = ip_bin[0:range] + "0"*(host_space)
mask = "1"*int(input1[1]) + "0"*host_space
#network = int(ip_bin[0])*int(ip_bin_mask[0]) + int(ip_bin[1])*int(ip_bin_mask[1]) + int(ip_bin[2])*int(ip_bin_mask[2])+ int(ip_bin[3])*int(ip_bin_mask[3]) + int(ip_bin[4])*int(ip_bin_mask[4]) +int(ip_bin[5])*int(ip_bin_mask[5])+int(ip_bin[6])*int(ip_bin_mask[6]) + int(ip_bin[7])*int(ip_bin_mask[7]) + int(ip_bin[8])*int(ip_bin_mask[8]) +int(ip_bin[9])*int(ip_bin_mask[9])+int(ip_bin[10])*int(ip_bin_mask[10]) + int(ip_bin[11])*int(ip_bin_mask[11]) + int(ip_bin[12])*int(ip_bin_mask[12]) +int(ip_bin[13])*int(ip_bin_mask[13])+int(ip_bin[14])*int(ip_bin_mask[14]) + int(ip_bin[15])*int(ip_bin_mask[15]) + int(ip_bin[16])*int(ip_bin_mask[16]) +int(ip_bin[17])*int(ip_bin_mask[17])+int(ip_bin[18])*int(ip_bin_mask[18]) + int(ip_bin[19])*int(ip_bin_mask[19]) + int(ip_bin[20])*int(ip_bin_mask[20]) +int(ip_bin[21])*int(ip_bin_mask[21])+int(ip_bin[22])*int(ip_bin_mask[22]) + int(ip_bin[23])*int(ip_bin_mask[23]) + int(ip_bin[24])*int(ip_bin_mask[24]) +int(ip_bin[25])*int(ip_bin_mask[25])+int(ip_bin[26])*int(ip_bin_mask[26]) + int(ip_bin[27])*int(ip_bin_mask[27]) + int(ip_bin[28])*int(ip_bin_mask[28]) +int(ip_bin[29])*int(ip_bin_mask[29])+int(ip_bin[30])*int(ip_bin_mask[30])+ int(ip_bin[30])*int(ip_bin_mask[30]) + int(ip_bin[31])*int(ip_bin_mask[31])
network = str(int(ip_bin[0])*int(ip_bin_mask[0])) + str(int(ip_bin[1])*int(ip_bin_mask[1])) + str(int(ip_bin[2])*int(ip_bin_mask[2]))+ str(int(ip_bin[3])*int(ip_bin_mask[3])) + str(int(ip_bin[4])*int(ip_bin_mask[4])) +str(int(ip_bin[5])*int(ip_bin_mask[5]))+str(int(ip_bin[6])*int(ip_bin_mask[6])) + str(int(ip_bin[7])*int(ip_bin_mask[7])) + str(int(ip_bin[8])*int(ip_bin_mask[8])) +str(int(ip_bin[9])*int(ip_bin_mask[9]))+str(int(ip_bin[10])*int(ip_bin_mask[10])) + str(int(ip_bin[11])*int(ip_bin_mask[11])) + str(int(ip_bin[12])*int(ip_bin_mask[12])) +str(int(ip_bin[13])*int(ip_bin_mask[13]))+str(int(ip_bin[14])*int(ip_bin_mask[14])) + str(int(ip_bin[15])*int(ip_bin_mask[15])) + str(int(ip_bin[16])*int(ip_bin_mask[16])) +str(int(ip_bin[17])*int(ip_bin_mask[17]))+str(int(ip_bin[18])*int(ip_bin_mask[18])) + str(int(ip_bin[19])*int(ip_bin_mask[19])) + str(int(ip_bin[20])*int(ip_bin_mask[20])) +str(int(ip_bin[21])*int(ip_bin_mask[21]))+str(int(ip_bin[22])*int(ip_bin_mask[22])) + str(int(ip_bin[23])*int(ip_bin_mask[23])) + str(int(ip_bin[24])*int(ip_bin_mask[24])) +str(int(ip_bin[25])*int(ip_bin_mask[25]))+str(int(ip_bin[26])*int(ip_bin_mask[26])) + str(int(ip_bin[27])*int(ip_bin_mask[27])) + str(int(ip_bin[28])*int(ip_bin_mask[28])) +str(int(ip_bin[29])*int(ip_bin_mask[29]))+str(int(ip_bin[30])*int(ip_bin_mask[30]))+ str(int(ip_bin[31])*int(ip_bin_mask[31]))

first_octet = int(mask[0])*128 + int(mask[1])*64 + int(mask[2])*32 + int(mask[3])*16 + int(mask[4])*8 + int(mask[5])*4 + int(mask[6])*2 + int(mask[7])*1
second_octet = int(mask[8])*128 + int(mask[9])*64 + int(mask[10])*32 + int(mask[11])*16 + int(mask[12])*8 + int(mask[13])*4 + int(mask[14])*2 + int(mask[15])*1
third_octet = int(mask[16])*128 + int(mask[17])*64 + int(mask[18])*32 + int(mask[19])*16 + int(mask[20])*8 + int(mask[21])*4 + int(mask[22])*2 + int(mask[23])*1
fourth_octet = int(mask[24])*128 + int(mask[25])*64 + int(mask[26])*32 + int(mask[27])*16 + int(mask[28])*8 + int(mask[29])*4 + int(mask[30])*2 + int(mask[31])*1
print(f'''
Network:
{int(network[0:8],2):<8} {int(network[8:16],2):<8} {int(network[16:24],2):<8} {int(network[24:32],2):<8} 
{ip_bin_mask[0:8]:<8} {ip_bin_mask[8:16]:<8} {ip_bin_mask[16:24]:<8} {ip_bin_mask[24:32]:<8}''')
print(f'''
Mask:
/{input1[1]}
{first_octet:<8} {second_octet:<8} {third_octet:<8} {fourth_octet:<8}
{mask[0:7]:<8} {mask[8:15]:<8} {mask[16:23]:<8} {mask[24:31]:<8} ''')

