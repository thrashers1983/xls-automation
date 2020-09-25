import clipboard
import os
from netmiko import SSHDetect
from netmiko import ConnectHandler

os.system("~/.mpass.sh")
otp = clipboard.paste()

r320 = {
    'device_type': 'cisco_wlc_ssh',
    'host': 'r320-wlc.rtl.apple.com',
    'username': 'yiping_feng',
    'password': otp,
    'conn_timeout': 30,
    'banner_timeout': 30,
    'auth_timeout': 30,
    'system_host_keys': True
    }

connect = ConnectHandler(**r320)
print(connect.send_command('show ap summary'))




