# 1.19. Transforming and Reducing Data at the Same Time
# 需求：想要执行一个reduction function(比如：sum(), min(), max())，但在这之前要先转换或者过滤数据
import os

# 把生成器表达式作为参数传给reduction function
# 例1
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# 例2
files = os.listdir('../data')
print(files)
if any(name.endswith('.py') for name in files):
    # endswith()判断字符串是否以指定后缀结尾，返回布尔值
    # any()函数的参数中的可迭代对象如果全部为False，则返回False，如果有一个为True，则返回True
    print('There be python!')
else:
    print('Sorry, no python.')

# 例3
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))
# join()方法用于将可迭代对象中的元素以指定的字符连接生成一个新的字符串

# 例4
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)

# 注：当把生成器表达式作为参数传给函数的时候，生成器表达式的()可以省略掉不写，以下两句话意思相同
s = sum((x * x for x in nums))
print(s)
s = sum(x * x for x in nums)
print(s)
