#for loop
family_members = ['yiping', 'kiphony', 'manman', 'tuntun', 'father', 'mother', 'mimi']
for member in family_members:
    print(member)
print()
for member in family_members:
    print(f'{member.title()}, welcome home.')
print('awesome, everybody home now.')
print()
#range()生成数字序列
for value in range(1, 5):
    print(value)
print()
for value in range(6):
    print(value)
print()
#用list()和range()生成数字列表
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)
######################################
squares = []
for value in range(1, 11):
#    square = value**2
#    squares.append(square)
    squares.append(value**2)
print(squares)
#对数字列表简单做一些统计
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
#用List Comprehensions生成列表
squares = [value**2 for value in range(1, 11)]      #value**2是一个表达式，表达式的计算结果填入list，for循环提供表达式需要的值
print(squares)
cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print(cube)
print()
#列表切片
sports = ['swimming', 'boxing', 'basketball', 'soccer', 'volleyball']
print(sports[0:3])
print(sports[1:4])
print(sports[:4])
print(sports[2:])
print(sports[-3:])
print(sports[::2])
#对切片做loop
for sport in sports[:3]:
    print(sport)
print()
#复制一个列表
my_foods = ['cake', 'bread', 'rice', 'noodle']
friends_foods = my_foods[:]     #生成一个新的列表，内容是my_foods的拷贝
# friends_foods = my_foods      这样写是错的，这等于是创建了一个链接，friends_foods和my_foods都指向了同一个列表
print(my_foods)
print(friends_foods)
print()
#tuple, tuple和list一样，但是tuple的内容不能改
#假设有一个长方形，长和宽是固定不变的，可以用tuple来存储长方形的长和宽
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#其实tuple是用逗号定义的，加括号是为了好看，如果tuple只有一个元素，后面还是要加一个逗号
tuple1 = 1, 2, 3
print(tuple1)
tuple2 = 4,
print(tuple2)
#tuple也可以循环
for dimension in dimensions:
    print(dimension)
#tuple的元素是不能改，但是可以重新定义一个tuple
dimensions = (150, 100)
for dimension in dimensions:
    print(dimension)
#python代码规范：
# 1. 缩进用4个空格，也可以直接tab，编辑器会把tab转化为4个空格
# 2. 每行长度不超过80个字符（这条规则不是那么严格）
# 3. 代码块之间用空行隔开，增加可阅读性

