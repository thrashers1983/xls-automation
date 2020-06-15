#if条件判断语句返回True或者False，返回True则执行if后面的代码，返回False就跳过if后面的代码
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#判断两个值是否相同是大小写敏感的，如果想忽略大小写，可以这样做：
# >>> user_name = 'John'
# >>> user_name == 'john'
# False
# >>> user_name.lower() == 'john'
# True
print()
#用!=判断不等于
requested_topping = 'beef'
if requested_topping != 'fish':
    print("Hold the fish!")
print()
#数字比较
answer = 18
if answer != 15:
    print('wrong answer, try again.')
if answer == 18:
    print('good boy.')
#其他数字比较符号：< <= > >=
# >>> age = 19
# >>> age < 21
# True
# >>> age <= 21
# True
# >>> age > 21
# False
# >>> age >= 21
# False
print()
#条件判断组合, and是两个条件都要true才返回true，or是两个条件只要一个是true就返回true
# >>> age_0 = 22
# >>> age_1 = 18
# >>> age_0 >= 21 and age_1 >= 21
# False
# >>> age_0 >= 21 or age_1 >= 21
# True
# 为了看的清楚，可以用括号把单个条件判断括起来：(age_0 >= 21) and (age_1 >= 21)
#
#用in判断一个item在列表中是否已存在
# >>> family_members = ['yiping', 'kiphony', 'manman', 'tuntun', 'father', 'mother', 'mimi']
# >>> 'yiping' in family_members
# True
# >>> 'xiaolaodi' in family_members
# False
#用not in判断一个item在列表中是否不存在
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
print()
#布尔表达式，布尔值要么是True，要么是False
game_active = True
if True:
    print('game is still running')
print()
#if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
print()
#if-elif-else语句
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")
print()
#含有多个elif的语句
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")
print()
#有时候在if-elif块的最后用elif比用else好
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")
print()
#if-elif-else语句适用于只对某一个条件感兴趣的情况，但有时候想检查所有的感兴趣的条件，这时就要用一系列if语句，不加elif和else
#if-elif-else语句块从上到下匹配，一旦匹配中一个条件，后面的就跳过了，单独的if语句则每一个if都要执行，每个if和之前的if没有关系
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
print()
#if语句和列表结合使用，比如在列表中找一个特殊的item
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
print()
#检查一个列表是否是空列表
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
print()
#多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
#available_toppings也可以是tuple，如果店家供应的toppings是稳定的话
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
print()
#python代码规范：
#写条件判断表达式的时候，在比较符号两边留空格，比如：if age < 4:

