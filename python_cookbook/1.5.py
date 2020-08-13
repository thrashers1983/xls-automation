# 1.5. Implementing a Priority Queue
# 需求：创建一个按优先级排列的队列，每次pop都返回一个具有最高优先级的item
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        # 我自己测了一把，如果是一个空列表用heapq.heappush()往里面添加元素，生成的列表就具有堆的特性(第一个元素总是最小的)，
        # 用heapq.heappop()弹出[0]号元素后，[0]号位会用次小的元素补位
        # 但如果是一个本来就有数据的列表，用heapq.heappush()添加元素，都是加在列表的最后
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        # Python中所有的类都直接或间接继承自object类，object类包含__repr__()方法，__repr__()是一个特殊方法，
        # 用来描述由类生成的实例对象本身，这里重写__repr__()方法，返回实例对象的名字
        return 'Item({!r})'.format(self.name)
        # !r对format()里的字符串调用repr()函数

xiaohong = Item('xiaohong')
print(xiaohong)

q = PriorityQueue()         # 生成PriorityQueue的一个实例
q.push(Item('foo'), 1)
print(q._queue)
q.push(Item('bar'), 5)
print(q._queue)
q.push(Item('spam'), 4)
print(q._queue)
q.push(Item('grok'), 1)
print(q._queue)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# 两个Item的实例是无法比较大小的，所以为每个实例加上priority，使之能够比较大小，考虑到priority可能一样，再引进index，
# 由于index的值唯一，所以一定能比出大小




