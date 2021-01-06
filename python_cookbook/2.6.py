# 2.6. Searching and Replacing Case-Insensitive Text
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))


# 下面用一个函数来实现替代的字符串匹配源字符串的大小写
def matchcase(word):
    # 这是一个嵌套函数，调用外层函数返回内层函数
    def replace(m):
        text = m.group()
        # re.sub()返回的第一个参数，也就是这里的m，是一个re.Match对象，用group()获取匹配到的字符串
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))
# 调用matchcase()返回内层函数replace，re.sub()把被pattern匹配到的内容作为参数传给replace函数

c = matchcase('jordan')
print(c.__closure__)
print(c.__closure__[0].cell_contents)
# 通过调用__closure__内置方法可以查看到两个内存地址，结果返回cell就是闭包，None则不是闭包
# 可以看出来其实这是一个元组类型，使用[0].cell_contents可以得到闭合数值，也就闭包所需要的环境变量

# 我自己总结的闭包使用场景：
# 当一个函数需要传入两个参数，并且这两个参数是先后由不同的人传入，可以使用闭包来实现
