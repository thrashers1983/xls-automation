# 1.16. Filtering Sequence Elements
# 需求： 根据条件过滤序列中的数据

# 用list comprehension
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
pos = [n for n in mylist if n > 0]
print(pos)
neg = [n for n in mylist if n < 0]
print(neg)

# 用generator expression
pos = (n for n in mylist if n > 0)      # 生成器表达式和列表推导式的语法区别就是把[]改成()
print(pos)                              # 得到一个生成器对象
for x in pos:
    print(x)

# 有时候过滤条件很复杂，比如需要处理exception，没法用列表推导式或生成器表达式搞定，这种情况可以写一个函数做条件判断，
# 再用内置函数filter()来过滤，举例如下：
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    # 自定义一个函数来做条件判断，返回True或False
    try:
        int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
# filter()接收两个参数，第一个参数是一个函数，第二个参数是一个序列，把序列中的每个元素作为参数传给这个函数去做判断，
# 函数返回True或False，filter()收集所有函数返回True的元素，返回一个迭代器
print(ivals)

# 列表推导式和生成器表达式也可以结合一些函数来做数据转换处理
import math

sqrt = [math.sqrt(n) for n in mylist if n > 0]
print(sqrt)

# 把不符合条件的值改一个值
clip_pos = [n if n > 0 else 0 for n in mylist]
print(clip_pos)
clip_neg = [n if n < 0 else 0 for n in mylist]
print(clip_neg)

# itertools.compress()的用法举例：
# 假设有两列数据，第一列是地址，第二列是地址出现的次数，一一对应，现在要选出地址出现次数大于5的地址
from itertools import compress

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]
print(more5)

addresses_more5 = list(compress(addresses, more5))
print(addresses_more5)
# itertools.compress()接收两个参数，第一个参数是一个可迭代对象，第二个参数是一个布尔值选择器序列，compress()函数
# 选出可迭代对象中所有对应的布尔值为True的元素，返回一个迭代器
