# 1.17. Extracting a Subset of a Dictionary

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}

# 用dictionary comprehension
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)

# 创建一系列的元组，把这些元组传给dict()函数
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)

# 换一种写法，还是用dictionary comprehension
p2 = {key: prices[key] for key in prices.keys() & tech_names}
print(p2)
