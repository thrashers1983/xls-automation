from chapter9_car import Car, ElectricCar
# 可以用别名，from chapter9_car import ElectricCar as EC
# 也可以import module_name，然后用模块名.类名来生成实例
# 也可以from module_name import *，这个不推荐

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.battery_size = 100
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
