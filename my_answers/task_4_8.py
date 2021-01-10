ip = '192.168.3.1'
ip_list = list(ip.split('.'))
print(f'''
      IP address:
      {ip_list[0]:<8} {ip_list[1]:<8} {ip_list[2]:<8} {ip_list[3]:<8}
      {int(ip_list[0]):08b} {int(ip_list[1]):08b} {int(ip_list[2]):08b} {int(ip_list[3]):08b}''')

