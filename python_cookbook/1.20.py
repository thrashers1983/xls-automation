# 1.20. Combining Multiple Mappings into a Single Mapping
# 使用场景：有多个字典，想要合并在一起，然后做一些操作比如查找某个值，或者检查某个键是否存在
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c)
print(c['x'])
print(c['y'])
print(c['z'])       # 如果有重复的key，则使用第一个字典里的键对应的值
print()

# ChainMap支持普通字典的操作
print(len(c))
print(list(c.keys()))
print(list(c.values()))
print()

# 对ChainMap做修改操作只会影响第一个字典
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# del c['y']    这句话会报错，因为第一个字典没有这个键
print()

values = ChainMap()
print(values)
values['x'] = 1
print(values)
values = values.new_child()         # new_child()方法添加一个新的映射
print(values)
values['x'] = 2
print(values)
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
values = values.parents             # parents方法丢弃最近一次添加的映射
print(values)
print(values['x'])
values = values.parents
print(values)
print()

# 用字典的update()方法也可以合并两个字典
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)        # 这里是生成一个新字典，也可以直接在原字典上用update()合并另外一个字典
print(merged)
merged.update(a)
print(merged)
print(merged['x'])
print(merged['y'])
print(merged['z'])
# 用这个方法合并产生的新字典和原来的字典没有关系，修改原字典不会影响合并后的新字典
a['x'] = 13
print(merged['x'])
print()
# ChainMap是使用的原字典，修改原字典会在ChainMap中有反映
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 42
print(merged['x'])
