# 1.12. Determining the Most Frequently Occurring Items in a Sequence
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)            # Counter的参数可以是任何由hashable对象组成的序列
print(word_counts)                      # Counter实际上是一个字典，key是序列中的item，value是该item出现的次数
print(word_counts['not'])
print(word_counts['eyes'])
top_three = word_counts.most_common(3)
print(top_three)

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print(word_counts)

word_counts.update(morewords)           # 用update()方法自动更新计数
print(word_counts)

# Counter实例支持数学运算符
a = Counter(words)
b = Counter(morewords)
print(a+b)
print(a-b)

# 以下是手动实现计数，我自己写的
word_counts = {}
for word in words:
    word_counts[word] = 0       # 手动创建字典的key
for word in words:
    word_counts[word] += 1
print(word_counts)
