# 一个简单的字典
kiphony = {'height': 166, 'weight': 55, 'face_value': 80}
print(kiphony['height'])
print(kiphony['weight'])
print(kiphony['face_value'])
print(f"Kiphony is {kiphony['height']} height, {kiphony['weight']}kg weight, and her face value is "
      f"{kiphony['face_value']}.")
# A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and
# you can use a key to access the value associated with that key. A key’s value can be a number,
# a string, a list, or even another dictionary. In fact, you can use any object that you can create
# in Python as a value in a dictionary.
print()
# 在字典中加入新的键值对
kiphony['breast'] = 'big'
kiphony['butt'] = 'booty'
print(kiphony)
print()
# 从空字典开始构造字典
yiping_son = {}
yiping_son['weight'] = 3
yiping_son['face'] = 'looks like her mother'
print(f"yiping's son was born, he is {yiping_son['weight']}kg weight, and he {yiping_son['face']}.")
print()
# 修改键对应的值
yiping_son['weight'] = 5
print(yiping_son)
print()
# 一个有趣的例子
tuntun = {'color': 'green', 'sex': 'male', 'speed': 'medium', 'position': 0}
if tuntun['speed'] == 'low':
    position_increment = 1
elif tuntun['speed'] == 'medium':
    position_increment = 2
elif tuntun['speed'] == 'fast':
    position_increment = 3
tuntun['position'] = tuntun['position'] + position_increment
# 这里pycharm提示说变量position_increment可能未被定义，这是因为如果if-elif所有条件判断语句都不匹配的话，这个变量就
# 无法被赋值，有两种方法解决这个提示：
# 1.在if语句之前先定义这个变量，给它随便赋一个值
# 2.if语句块的最后用else匹配其余所有条件
print(f"now tuntun's position is {tuntun['position']}")
print()
# 删除键值对
print(tuntun)
del tuntun['sex']
print(tuntun)
print()
# 字典可以是同一个对象的各种属性信息，也可以是许多对象的同一类型的信息
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# 这是写字典的另一种格式，每一个键值对一行，并且每一个键值对都缩进一个level，在最后的键值对的后面加一个逗号，这是好习惯
print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")
print()
# 对于字典，还可以用get()方法访问一个键，如果这个键存在，则正常返回该键对应的值，如果这个键不存在，则可以返回一个默认值，
# 这样做的目的是，如果访问了一个不存在的键，程序不会报错
favorite_language = favorite_languages.get('mike', 'swift')
print(favorite_language)
# get()的第一个参数是想要访问的键，第二个参数可选，是想要返回的默认值，如果不写就返回None
print()
# loop键值对
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
# items()方法其实是返回一个键值对的列表，然后for loop把键和值分别赋给name和language这两个变量
print()
# loop键
for name in favorite_languages.keys():
    print(name.title())
print()
# 实际上loop键是loop一个字典的默认行为，所以也可以不写keys()
for name in favorite_languages:
    print(name.title())
print()
# 只loop键，然后通过键访问对应的值
for name in favorite_languages.keys():
    language = favorite_languages[name]
    print(f"Hi {name.title()}, I see you love {language.title()}!")
print()
# 判断字典中是否有某个键
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
# keys()方法返回一个键的列表，然后检查erin是否在这个列表中
print()
# 按特殊的顺序loop键
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
print()
# loop值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# values()方法返回一个值的列表，注意python出现了2次
print()
# 字典的键是唯一的，但是值有可能重复，可以用set()来创建一个无序的不重复的元素集
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
print()
# 也可以用{}直接创建一个set
languages = {'python', 'ruby', 'python', 'c'}
print(languages)
print()
# list,tuple,set,dictionary的辨识：
# tuple和list都是有序列表，list是可变对象，tuple是不可变对象，set是没有重复元素的无序列表，set和dictionary都用大括号
# 包裹，容易搞混，dictionary有键值对，set都是单个元素

# 列表嵌套字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print()
# 自动生成alien
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
print()
# 修改前三个alien的属性
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[:5]:
    print(alien)
print("...")
print()
# 字典嵌套列表
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
print()
# 字典嵌套列表例子2
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'java'],
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is: {languages[0].title()}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
print()
# 字典嵌套字典
users = {
    'ypfeng': {
        'first': 'yiping',
        'last': 'feng',
        'location': 'shanghai',
    },
    'sjwang': {
        'first': 'sijie',
        'last': 'wang',
        'location': 'suzhou',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
