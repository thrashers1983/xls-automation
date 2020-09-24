# 1.15. Grouping Records Together Based on a Field
# 需求：假设有一个由字典组成的列表，现在想按字典某一个键的值来分组
from operator import itemgetter
from itertools import groupby

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key=itemgetter('date'))
print(rows)

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

# 每一次迭代，groupby()会扫描序列中的连续相同的元素(这个例子中每个元素是一个字典)，如果提供了key参数，则扫描key参数返回的值
# 中连续相同的值，按这个相同的值把该值对应的列表元素分组，返回这个值和对应的分组，由于groupby()只检查连续的item，所以这个例子
# 中要先把序列sort一把，把相同的date排到一起
print()

# 下面这个方法可以实现相同的功能
from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)
