# 1.2. Unpacking Elements from Iterables of Arbitrary Length
user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
# *解包操作不能单独使用，如果写*phone_numbers = user_record程序会报错，可以这样写：*phone_numbers, = user_record
# 这里的phone_numbers变量总是一个列表，如果没有元素就是空列表
print(name, email, *phone_numbers, phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(*trailing, trailing, current)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(*para):          # 这个*号的作用是接受任意数量的参数，把收到的参数放进para这个元组里
    print('foo', para)
    print('foo', *para)     # 这个*号的作用是把可迭代对象中的元素解包出来


def do_bar(*para):
    print('bar', *para)


for tag, *args in records:
    if tag == 'foo':
        print(*args, args)
        do_foo(*args)       # 这个*号把可迭代对象args里的元素解包出来以位置参数的方式传给函数
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, home_dir, sh = line.split(':')
print(uname, home_dir, sh, fields)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


digits = [1, 10, 7, 4, 5, 9]
results = sum(digits)
print(results)

# *和**详解：
# 在调用函数的时候：
# *的作用是将*后面的可迭代对象解包出来，按位置参数的方式传给函数
# **的作用是将**后面的字典里的键值对按命名参数的方式传给函数
# 在定义函数的时候：
# *的作用是接收任意数量的位置参数，把他们按顺序加到一个元组里
# **的作用是接收任意数量的命名参数，把他们按键值对加入一个字典里
# 举例如下：


def asterisk_1(*para):
    print(para)


def asterisk_2(para1, para2):
    print(para1, para2)


def asterisk_3(**para):
    print(para)


def asterisk_4(x, y):
    print(x, y)


args = (1, 2)
asterisk_1(1, 2)
asterisk_1(*args)
asterisk_2(1, 2)
asterisk_2(*args)

arg_dict = {'x': 1, 'y': 2}
asterisk_3(x=1, y=2)
asterisk_3(**arg_dict)
asterisk_4(x=1, y=2)
asterisk_4(**arg_dict)
