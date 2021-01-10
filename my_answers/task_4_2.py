mac = "AAAA:BBBB:CCCC"
mac2 = list(mac.split(':'))
print('Firts way ' + '.'.join(mac2),'\nSecond way '+ mac.replace(':','.'))
