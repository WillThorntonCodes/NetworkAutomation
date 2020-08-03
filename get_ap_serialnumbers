# Get serial numbers of APs from WLC

from netmiko import ConnectHandler
import re

my_wlc = {
    'device_type': 'cisco_wlc_ssh',
    'host': '1.1.1.1', 
    'username': 'UserName',
    'password': 'PassW0rd!',       
}

conn = ConnectHandler(**my_wlc)
answer = conn.send_command('show ap inventory all')

result = re.findall('PID: (.*)',answer)
for device in result:
    x = str(device).replace('  VID: V01,  ','')
    print (x)
