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
_, shares, price, _ = data
print(shares, price)
