# 2.3. Matching Strings Using Shell Wildcard Patterns
from fnmatch import fnmatch, fnmatchcase

# 用通配符来匹配文件名
print(fnmatch('foo.txt', '*.txt'))          # *匹配任意多个字符
print(fnmatch('foo.txt', '?oo.txt'))        # ?匹配任意单个字符
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))    # [0-9]匹配单个数字

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
csv_file = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(csv_file)

print(fnmatch('foo.txt', '*.TXT'))
# fnmatch()的大小写敏感规则和操作系统的大小写敏感规则一样，macos对大小写敏感，windows对大小写不敏感
# 可以用fnmatchcase()强制大小写敏感匹配
print(fnmatchcase('foo.txt', '*.TXT'))

# 用通配符匹配非文件名的字符串
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

address = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(address)
address = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(address)

# fnmatch()使用场景：当匹配机制不是很复杂以至于要用正则表达式的时候，使用fnmatch()用通配符来匹配是个不错的选择
