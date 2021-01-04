# 2.4. Matching and Searching for Text Patterns
import re

# 如果想要匹配简单的文本，可以用基本的字符串方法
text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))
print()

# 做复杂匹配，用正则表达式
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# 把正则表达式预编译为一个pattern对象
datepat = re.compile(r'\d+/\d+/\d+')
print(type(datepat))

if datepat.match(text1):        # re.match(pattern, string)的写法改成pattern.match(string)
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

# match()尝试从字符串的起始位置开始匹配，如果在起始位置没有匹配到就返回None
# 如果要找出字符串中所有的被pattern匹配到的文本，用findall()函数，findall()返回一个列表
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.match(text))
print(datepat.findall(text))
print()

# 把pattern的某些部分放到捕获组中，后续可以很方便的提取匹配到的内容
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m)
print(m.group())
print(m.group(0))       # 可以看到，group()和group(0)捕获的都是整个匹配到的内容
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month, day, year = m.groups()
print(month)
print(day)
print(year)
print()

# 如果pattern中有捕获组，findall()函数只返回匹配到的文本里的捕获组里的内容
print(datepat.findall(text))
# 如果pattern中有捕获组，又希望findall()返回整个匹配到的内容，则要在捕获组前加?:使之成为非捕获组
print(re.findall(r'(?:\d+)/(?:\d+)/(?:\d+)', text))

for month, day, year in datepat.findall(text):
    print(f'{year}-{month}-{day}')

print()
# finditer()和findall()功能类似，不过返回的是一个迭代器
print(datepat.finditer(text))

for m in datepat.finditer(text):
    print(m)        # 每次迭代，得到一个re.Match对象
    print(m.group())
    print(m.groups())
