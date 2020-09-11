# 把字符串赋给一个变量，可以用单引号，也可以用双引号
new_message = 'this is master branch'
news_2020 = "kiphony has now become yiping's girlfriend."
print(new_message)
print(news_2020)
print()
# title(),upper(),lower()的使用
girlfriend_name = 'kiphony yu'
print(girlfriend_name.title())
print(girlfriend_name.upper())
print(girlfriend_name.lower())
print()
# f-string的使用
first_name = "yiping"
last_name = "feng"
full_name = f"{first_name} {last_name}"
print(full_name.title())
print(f"Hello, {full_name.title()}, how are you?")
greetings = f"Hello, {full_name.title()}, how are you?"
print(greetings)
print()
# \t,\n的使用
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
print()
# rstrip(),lstrip(),strip()的使用
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
favorite_language = favorite_language.rstrip()
print(favorite_language)
favorite_language = ' ruby\n\t'
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
print()
# 整数运算
addition = 2+3
subtraction = 3-2
multiplication = 2*3
division = 3/2
print(addition)
print(subtraction)
print(multiplication)
print(division)
exponents = 3**3
print(exponents)
multiple_operations = 2+3*4
print(multiple_operations)
multiple_operations = (2+3)*4
print(multiple_operations)
print()
# 浮点数运算，忽略后面多出来的小数位
add = 0.2+0.1
sub = 0.2-0.1
mul = 3*0.1
div = 2/0.1
print(add)
print(sub)
print(mul)
print(div)
print()
# 整数和浮点数一起算
add = 1+2.0
mul = 2*3.0
div = 4/2
exp = 3.0**2
print(add)
print(mul)
print(div)
print(exp)
print()
# 对于很大的数字，可以用下划线分隔，这样容易阅读
universe_age = 14_000_000_000
print(universe_age)
print()
# 一行赋值多个变量
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
# 如果一个变量的值永远不会变，建议用大写字母来定义，这不是强制的，只是约定俗成的习惯
MAX_CONNECTIONS = 5000
