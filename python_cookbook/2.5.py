# 2.5. Searching and Replacing Text
import re
from calendar import month_abbr

# 对于简单的文本替换，用str.replace()方法
text = 'yeah, but no, but yeah, but no, but yeah'
text_replace = text.replace('yeah', 'yep')
print(text_replace)

# 对于复杂的匹配，用sub()函数
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))      # \1，\2，\3引用前面的捕获组

# 如果要重复做相同的替换，可以先预编译pattern
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))


# 对于更复杂的替换，可以定义函数来实现，把这个函数作为re.sub()的第二个参数，如下例子：
# 定义一个函数，把月份改成英文缩写的形式，这个函数将作为re.sub()的第二个参数，接受re.sub()的第一个参数作为其参数
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


print(datepat.sub(change_date, text))

# 如果想替换并查看替换次数，用re.subn()函数
print(datepat.subn(r'\3-\1-\2', text))      # re.subn()返回一个元组，第一个元素是替换后的字符串，第二个元素是替换的次数
new_text, n = datepat.subn(r'\3-\1-\2', text)
print(new_text)
print(n)
