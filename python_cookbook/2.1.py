# 2.1. Splitting Strings on Any of Multiple Delimiters
# 需求：分隔符没有规律，要用正则来匹配
import re

line = 'asdf fjdk; afed, fjek,asdf,     foo'
fields = re.split(r'[;,\s]\s*', line)
print(fields)
# re.split()的第一个参数是正则表达式pattern，第二个参数是原始字符串，r指定后面的字符串就是纯字符串，在这里其实没用，不加r也行

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
# 如果把pattern放到捕获组中，也就是放到()中，那么被()中的pattern匹配到的分隔符也会返回到结果中

# 保留分隔符有时候也有用，比如想要用同样的分隔符来重新构造原始字符串
values = fields[::2]
print(values)
delimiters = fields[1::2] + ['']
print(delimiters)

new = ''.join(v+d for v, d in zip(values, delimiters))
print(new)

# 如果不想分隔符出现在返回结果中，但是仍然想把pattern放在()中，则要使用非捕获组(?:)
fields = re.split(r'(?:,|;|\s)\s*', line)
print(fields)
