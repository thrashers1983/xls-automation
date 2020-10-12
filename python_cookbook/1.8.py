# 1.8. Calculating with Dictionaries
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
print(prices.values())
print(prices.keys())
for item in zip(prices.values(), prices.keys()):
    print(item)
print()
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# zip()返回的迭代器对象只能被使用一次
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
# print(max(prices_and_names))        # 这里会报错说max()的参数是空序列

print(min(prices))              # 只比较key
print(max(prices))

print(min(prices.values()))     # 只比较value
print(max(prices.values()))

print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))
# 对字典用min()，max()之类的函数，默认是比较字典的key，所以这里的lambda函数的参数是k是字典的key，比较value，返回结果对应的key

min_value = prices[min(prices, key=lambda k: prices[k])]    # 根据key再得到对应的value

# 利用zip()函数反转字典得到一系列(value, key)组成的tuple，对这些tuple做比较会先比较value，value如果有重复值，再比较key
# 举例如下：
prices = {'AAA': 45.23, 'ZZZ': 45.23}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
