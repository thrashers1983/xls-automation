# 1.9. Finding Commonalities in Two Dictionaries
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print(a.keys() & b.keys())      # 找两个字典里相同的key
print(a.keys() - b.keys())      # 找a有但b没有的key
print(a.items() & b.items())    # 找两个字典里相同的(key, value)
# keys()返回key的集合，items()返回(key, value)的集合，他们都支持直接使用set的一些操作比如& -
# values()不支持set的操作，原因之一是values()里可能有重复值
# 如果想要对values()做set操作，只能先把values()返回的对象转换成set，再执行set操作：
print(set(a.values()) & set(b.values()))
print(set(a.values()) - set(b.values()))

# 用dictionary comprehension生成字典
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
