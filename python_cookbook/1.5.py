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
        # !r表示对format()里的字符串调用repr()方法，上面这行代码等价于return 'Item({})'.format(repr(self.name))


zhang_hong = Item('zhang hong')
print(zhang_hong)
# 创建了类的一个实例，由于这个类只重构了__repr__()方法，所以这个实例调用类的__repr__()方法来返回一个值，如果没有重构
# __repr__()方法，应该是会调用父类的__str__()方法来返回一个值

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

# 对一个对象调用str()方法，实际上是调用这个对象自己的__str__()方法
# 对一个对象调用repr()方法，实际上是调用这个对象自己的__repr__()方法
# 举例如下：
string = '123'
print(str(string))
print(string.__str__())
print(repr(string))
print(string.__repr__())
