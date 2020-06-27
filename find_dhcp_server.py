# Find if a Cisco router or switch has DHCP configured
# Error will only return the IP of the device where the program failed

from netmiko import ConnectHandler

list_ = open("deviceList.txt").read().split()
for x in list_:
    try:
        ios = {
            'device_type': 'cisco_ios',
            'ip': x,
            'username': 'username',
            'password': 'password',
        }
        net_connect = ConnectHandler(**ios)
        result = net_connect.send_command('sh run | inc pool')
        if 'pool' in result:
            print (x)
        else:
            print("No DHCP server on "+x)
    except:
        exception = open("errorlog.txt","a")
        exception.write(x+"\n")
