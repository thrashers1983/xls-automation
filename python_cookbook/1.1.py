# 1.1. Unpacking a Sequence into Separate Variables
p = (4, 5)
x, y = p
print(x, y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)
name, shares, price, (year, mon, day) = data
print(name, shares, price, year, mon, day)

s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data      # 如果解包的时候有些值不想要，可以随便用一个没有其他用途的变量去接，书里的例子用的是_
print(shares, price)
