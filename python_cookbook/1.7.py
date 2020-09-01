# 1.7. Keeping Dictionaries in Order
from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

d_json = json.dumps(d)      # json.dumps(d)的作用是把字典转换成字符串
print(d_json)

# 用OrderedDict构建的字典是有序字典，其遵循插入顺序来对键值对排序
# python3.6以后普通字典也是有序的，所以OrderedDict现在已经没用了
