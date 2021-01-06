# 2.7. Specifying a Regular Expression for the Shortest Match
import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))

# .*是贪婪匹配，.*?是非贪婪匹配，以上面的例子来说，\"(.*)\"的匹配行为是定位第一个"直到字符串末尾，然后从末尾向前找直到找到第一个"，
# 匹配两个"中的所有内容，\"(.*?)\"的匹配行为是找第一个"和下一个"，匹配两个"中的所有内容，再用同样的行为继续往下匹配直到字符串结束
# 由于pattern中有捕获组，findall()仅返回捕获组的内容
