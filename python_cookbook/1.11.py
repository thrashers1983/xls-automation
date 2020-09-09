# 1.11. Naming a Slice
# 有一种场景：需要从一个record(record可能是字符串或其他相似的格式)里切片出来数据，这些数据在字符串中的位置是固定的
# 比如有一个字符串变量名字叫record，里面记录了持有股票的数量[20:32]和股价[40:48]，要计算总市值：
# cost = int(record[20:32]) * float(record[40:48])
# 这样写可阅读性很差，等以后再看代码的时候就不知道[20:32]和[40:48]是什么意思，取而代之可以给切片命名：
# SHARES = slice(20, 32)
# PRICE = slice(40, 48)
# cost = int(record[SHARES]) * float(record[PRICE])

# slice()方法创建一个切片对象，这个切片对象可以在之后被使用
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)

# slice实例的三个属性：
a = slice(10, 50, 2)
print(a.start)          # 开始
print(a.stop)           # 结束
print(a.step)           # 步进

# 用slice实例的indices(size)方法把slice实例映射到一个特定大小的序列上，返回一个三元组的值不超过该序列的边界
a = slice(5, 20, 2)
s = 'HelloWorld'
b = a.indices(len(s))
print(b)
for i in range(*b):
    print(s[i])
