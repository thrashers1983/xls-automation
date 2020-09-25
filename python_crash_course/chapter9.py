# 创建一个狗的类，类名的首字母大写，在类里面用def定义的函数(function)称为方法(method)，__init__()是一个特殊方法，
# 当基于一个类生成一个实例的时候，python会自动调用__init__()方法，self在调用方法的时候自动传递，表示创建的实例本身，
# self.开头的变量可以被类中所有的方法访问，我们也可以通过从类生成的实例访问这些变量，self.name = name把参数的值赋值
# 给了变量，这个变量是实例的属性，类中的其他方法也都有self参数，在调用方法的时候self自动传递
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# 生成一个狗的实例
my_dog = Dog('Willie', 6)
# 生成Dog类的实例，python读到这行会自动调用Dog类的__init__()方法，并传递'Willie'和6这两个argument，__init__()方法
# 创建一个实例并把我们提供的参数值赋给self.name和self.age，然后返回一个实例代表这个特殊的狗，这里把实例赋给变量my_dog，
# 首字母大写代表类名，实例名全小写字母
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
# 实例的属性可以通过实例名.属性名访问，实例也可以通过实例名.方法名调用类的方法
print()


# 创建一个车的类
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        # 当创建一个实例的时候，实例的属性不一定要通过参数传递，也可以在__init__()方法中定义属性的默认值

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
print()

# 改变属性值方法1：直接修改实例属性
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 改变属性值方法2：通过调用方法修改属性值
my_new_car.update_odometer(24)
my_new_car.read_odometer()
print()

# 改变属性值方法3：通过调用方法增量更新属性值
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
print()


# 创建电动车类，继承自车类，电动车类是车类的子类，车类是电动车类的父类，子类可以继承父类的属性和方法，也可以定义子类自己的
# 属性和方法，当要创建一个子类的时候，父类必须也在当前这个文件中，并且必须出现在子类的前面，定义子类时，父类的名字要写在括
# 号里，super()是一个特殊函数，在创建子类实例的时候，super()会调用父类的__init__()方法，把其中定义的属性给子类的实例
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        # 定义子类特有的属性

    def describe_battery(self):
        # 定义子类特有的方法
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
# 创建ElectricCar的实例，调用ElectricCar的__init__()方法，继而调用父类Car的__init__()方法
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
# 如果父类的某一个方法不适用于子类，则可以在子类里定义一个同名的方法，这样这个继承下来的父类方法就在子类中被重写了
print()


# 把一个大类划分成几个小类，比如电动车类里还可以有电池类，可以把电池类的一个实例作为电动车类的一个属性
# 创建电池类，并且把describe_battery()方法挪到Battery类里
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            battery_range = 260
        elif self.battery_size == 100:
            battery_range = 315
        print(f"This car can go about {battery_range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery = Battery(100)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# 这里my_tesla是ElectricCar的一个实例，my_tesla.battery是my_tesla实例的属性，同时也是Battery类的一个实例
# my_tesla.battery = Battery(100)等于是创建一个Battery类的实例，同时修改了my_tesla.battery属性的值
# my_tesla.battery.describe_battery()等于是通过my_tesla.battery这个Battery的实例调用了Battery类的一个方法

# 代码规范：
# 类名首字母大写，不要加下划线，实例名和模块名用小写和下划线组合，类的方法之间空一行，类和类之间空两行，类和模块都要写
# docstring，如果要import标准库中的模块和自己写的模块，先import标准库，然后空一行，再import自己写的模块
