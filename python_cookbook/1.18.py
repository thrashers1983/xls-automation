# 1.18. Mapping Names to Sequence Elements
# 用名字访问序列元素
from collections import namedtuple
# collections.namedtuple()是一个工厂函数，返回一个tuple类的子类

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

# namedtuple的实例也支持普通tuple的操作：
print(len(sub))
addr, joined = sub
print(addr)
print(joined)
print(sub[0])
print(sub[1])
print()

# namedtuple的使用场景：
# 假设有一个列表包含了一些元组
stocks = [
    ('ACME', 1000, 45.23),
    ('AAPL', 2000, 612.78),
    ('IBM', 1500, 205.55),
    ('HPQ', 2500, 37.20),
    ('FB', 3000, 10.75)
]


# 定义一个用普通tuple实现的函数，可以看到，根据位置来引用tuple元素很不直观
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


total_value = compute_cost(stocks)
print(total_value)


# 改用namedtuple来实现
Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


total_value = compute_cost(stocks)
print(total_value)
print()

# namedtuple和普通tuple一样，是不可变对象，如果想改变元素，用_replace()方法，该方法返回一个全新的namedtuple实例
s = Stock('GOOGl', 1000, 123)
print(s)
s = s._replace(price=100)
print(s)
print()

# _replace()的巧妙用法：
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)
# 先创建一个namedtuple实例原型，给每个元素一个默认值，后续用_replace()来替换相应的值以创建新的实例


def dict_to_stock(s):       # 定义一个函数用来把字典转换成namedtuple
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
