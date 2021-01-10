mac = "AAAA:BBBB:CCCC"
hex_only = mac.split(':')
print(hex_only[0].replace('A','1010')+hex_only[1].replace('B','1011')+hex_only[2].replace('C','1100'))
