# 列表中的字典数据写入到csv表
import csv

headers = ['class', 'name', 'sex', 'height', 'year']

rows = [
    {'class': 1, 'name': 'xiaoming', 'sex': 'male', 'height': 168, 'year': 23},
    {'class': 1, 'name': 'xiaohong', 'sex': 'female', 'height': 162, 'year': 22},
    {'class': 2, 'name': 'xiaozhang', 'sex': 'female', 'height': 163, 'year': 21},
    {'class': 2, 'name': 'xiaoli', 'sex': 'male', 'height': 158, 'year': 21},
]

with open('test.csv', 'a') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
