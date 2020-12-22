# 1.5. Implementing a Priority Queue
# 需求：创建一个按优先级排列的队列，每次pop都返回一个具有最高优先级的item
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        # 对一个列表调用heapq.heappush()往里面添加元素，生成的列表就具有堆的特性(第一个元素总是最小的)，
        # 用heapq.heappop()弹出[0]号元素后，[0]号位会用次小的元素补位
        # 单纯两个item是无法比较大小的，所以为每个item加上priority，使之能够比较大小，考虑到priority可能一样，
        # 再引进index，由于index的值唯一，所以一定能比出大小
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    # Python中所有的类都直接或间接继承自object类，object类包含__str__()方法和__repr__()方法，这两个都是特殊方法，
    # 用来描述由类生成的实例对象本身，这里重写__str__()方法和__repr__()方法，返回实例对象的名字
    def __str__(self):
        return 'Item({!s})'.format(self.name)
        # !s表示对format()里的字符串调用str()方法，上面这行代码等价于return 'Item({})'.format(str(self.name))
        # 注意，str(self.name)是对self.name这个对象调用str()，self.name如果是个字符串，那就是对字符串对象调用str()，
        # 和这里重构的__str__()方法没有任何关系

    def __repr__(self):
        return 'Item({!r})'.format(self.name)
        # !r表示对format()里的字符串调用repr()方法，上面这行代码等价于return 'Item({})'.format(repr(self.name))
        # 注意，repr(self.name)是对self.name这个对象调用repr()，self.name如果是个字符串，那就是对字符串对象调用repr()，
        # 和这里重构的__repr__()方法没有任何关系


zhang_hong = Item('zhang hong')         # 生成Item的一个实例
print(zhang_hong)
print(str(zhang_hong))
print(repr(zhang_hong))
# 从以上print输出结果看，print()和print(str())的输出结果一样，可见打印的时候，由于输出是给人看的，所以默认调用实例对象的
# __str__()方法来描述对象

q = PriorityQueue()         # 生成PriorityQueue的一个实例
q.push(Item('foo'), 1)
print(q._queue)
q.push(Item('bar'), 5)
print(q._queue)
q.push(Item('spam'), 4)
print(q._queue)
q.push(Item('grok'), 1)
print(q._queue)
# 这里可以看到，被插入列表中的Item类的实例是带引号的，也证实了在开发调试过程中对象会调用__repr__()来描述自己

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
# 这里可以看到，pop出来的Item类实例，显示是不带引号的

# str()和repr()都用于将某一类型的变量转换为字符串对象，他们之间的不同点举例如下：
from datetime import datetime
now = datetime.now()
print(type(now))
print(type(str(now)))
print(type(repr(now)))
print(now)
print(str(now))         # str()的输出追求可读性，适合人类阅读，和直接print的输出结果一样
print(repr(now))        # repr()的输出包含了对象的数据类型信息，适合开发和调试阶段使用
# 再举一个例子：
string = '123'
print(type(string))
print(type(str(string)))
print(type(repr(string)))
print(string)
print(str(string))      # str()的输出不带引号，和直接print的输出结果一样
print(repr(string))     # repr()的输出带引号

# 对一个对象调用str()方法，实际上是调用这个对象自己的__str__()方法
# 对一个对象调用repr()方法，实际上是调用这个对象自己的__repr__()方法
print(now.__str__())
print(now.__repr__())
print(string.__str__())
print(string.__repr__())
