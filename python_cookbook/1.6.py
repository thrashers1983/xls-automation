# 1.6. Mapping Keys to Multiple Values in a Dictionary
# 需求：创建一个字典，字典的每个键对应多个值
from collections import defaultdict

# 方法1：创建普通的字典，把value放在list或者set中
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

# 方法2：用defaultdict创建字典
d = defaultdict(list)
print(d)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
print(d['a'])
print(d['b'])
print(d['c'])           # 读一个不存在的key，字典自动为这个key创建一个默认的value为空列表
print(d)                # 这时候字典已经有了c这个key，对应的value是[]

d = defaultdict(set)
print(d)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)
print(d['a'])
print(d['b'])
print(d['c'])           # 读一个不存在的key，字典自动为这个key创建一个默认的value为空set
print(d)                # 这时候字典已经有了c这个key，对应的value是set()

# 用defaultdict创建的字典，会自动为key创建默认的value(空列表，空set，空字符串)，普通字典需要手动给key分配value，
# 下面这两个示例可以看出使用defaultdict的代码更加简洁
# d = {}
# for key, value in pairs:
#     if key not in d:
#         d[key] = []
#     d[key].append(value)
#
# d = defaultdict(list)
# for key, value in pairs:
#     d[key].append(value)
