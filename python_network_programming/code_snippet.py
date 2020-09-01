# globalval=6
#
# def checkglobalvalue():
#     return globalval
#
# def localvariablevalue():
#     global globalval
#     globalval=8
#     return globalval
#
# print ("This is global value",checkglobalvalue())
# print ("This is global value",globalval)
# print ("This is local value",localvariablevalue())
# print ("This is global value",globalval)


# import sys
#
# print("Total output is ")
# print(int(sys.argv[1])+int(sys.argv[2]))        # 从命令行传进来的参数是字符串格式
# print(f"script name is:\n{sys.argv[0]}")


# import datetime
# from threading import Thread
#
#
# def checksequential():
#     for n in range(1, 10):
#         print(datetime.datetime.now().time())
#
#
# def checkparallel():
#     print(str(datetime.datetime.now().time())+"\n")
#
#
# checksequential()
# print("\nNow printing parallel threads\n")
# threads = []
# for x in range(1, 10):
#     t = Thread(target=checkparallel)
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()


# from netmiko import ConnectHandler
#
# device = ConnectHandler(device_type='juniper_junos', ip='221.224.146.78', username='yiping_feng',
#                         password='Bechtel1@34')
# output = device.send_command("show system uptime")
# print(output)
# device.disconnect()


# from netmiko import SSHDetect
# # 自动探测设备类型
# # dtd = device to detected
# # dbd = device being detected
#
# dtd = {
#     'device_type': 'autodetect',
#     'host': '192.168.100.51',
#     'username': 'yiping_feng',
#     'password': '111111'
#     }
#
# dbd = SSHDetect(**dtd)
# result = dbd.autodetect()
# print(result)


# from netmiko import ConnectHandler
#
# print("Before config push:")
# device = ConnectHandler(device_type='cisco_ios', ip='192.168.100.51', username='yiping_feng',
#                         password='111111')
# output = device.send_command("show running-config interface gigabitEthernet 1")
# print(output)
#
# configcmds = ["interface gigabitEthernet 1", "description home network"]
# device.send_config_set(configcmds)
#
# print("After config push:")
# output = device.send_command("show running-config interface gigabitEthernet 1")
# print(output)
# device.send_command("write memory")
#
# device.disconnect()


from netmiko import ConnectHandler

device = ConnectHandler(device_type='cisco_ios', ip='192.168.100.51', username='yiping_feng',
                        password='111111')

def task1():
    output = device.send_command("show version")
    print(output)
    output = device.send_command("show ip int brief")
    print(output)
    output = device.send_command("show clock")
    print(output)
    output = device.send_command("show running-config | in username")
    output = output.splitlines()
    for item in output:
        item = item.split(" ")
        print(f"username configured: {item[1]}")

def task2():
    global device
    configcmds = ["username test privilege 15 secret test"]
    device.send_config_set(configcmds)
    output = device.send_command("show running-config | in username")
    output = output.splitlines()
    for item in output:
        item = item.split(" ")
        print(f"username configured: {item[1]}")
    device.disconnect()
    try:
        device = ConnectHandler(device_type='cisco_ios', ip='192.168.100.51', username='test',
                                password='test')
        print("Authenticated successfully with username test")
        device.disconnect()
    except:
        print("Unable to authenticate with username test")

def task3():
    device = ConnectHandler(device_type='cisco_ios', ip='192.168.100.51', username='test',
                            password='test')
    output = device.send_command("show running-config | in username")
    output = output.splitlines()
    for item in output:
        if ("test" not in item):
            item = item.split(" ")
            device.send_command_timing("conf t")
            prompt = device.send_command_timing(f"no username {item[1]}")
            if "[confirm]" in prompt:
                device.send_command_timing("\n")
            device.send_command_timing("end")
    output = device.send_command("show running-config | in username")
    output = output.splitlines()
    for item in output:
        item = item.split(" ")
        print(f"username configured: {item[1]}")

    device.disconnect()


task3()

