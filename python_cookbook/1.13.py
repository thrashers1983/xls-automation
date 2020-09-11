# 1.13. Sorting a List of Dictionaries by a Common Key
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

a = itemgetter('lname', 'fname')
for row in rows:
    print(a(row))

# itemgetter()的功能用lambda表达式也能实现，itemgetter()的执行速度更快一点
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
print(rows_by_fname)
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
print(rows_by_lfname)

b = lambda r: (r['lname'], r['fname'])
for row in rows:
    print(b(row))

# itemgetter()也可以用于min()，max()
print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))
