# 2.2. Matching Text at the Start or End of a String
import os
from urllib.request import urlopen
import re

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

filenames = os.listdir('../data')
print(filenames)
filename = [name for name in filenames if name.endswith(('.png', '.json'))]
# 如果有多个匹配条件，把他们放到一个元组中传给startswith()或者endswith()
print(filename)
print(any(name.endswith('.txt') for name in filenames))


# 下面这个函数是书上随便举的一个例子，有用到startswith()方法
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


url = 'http://h2020.myspecies.info'
x = read_data(url)
print(x)

# 同样的功能也可以用正则表达式来实现
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))
