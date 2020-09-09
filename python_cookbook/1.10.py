# 1.10. Removing Duplicates from a Sequence while Maintaining Order
def dedupe_1(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
no_dup = list(dedupe_1(a))
print(no_dup)


def dedupe_2(items):
    seen = []
    nodup = []
    for item in items:
        if item not in seen:
            nodup.append(item)
            seen.append(item)
    return nodup


b = [1, 5, 2, 1, 9, 1, 5, 10]
no_dup = dedupe_2(b)
print(no_dup)
# 上面这两个函数都实现了相同的去重功能，dedupe_1是一个生成器，每次执行吐一个值出来，循环是在list()调用生成器的时候做的，
# dedupe_2是一个普通函数，一次执行完就把没有重复的列表返回回来了，这两个函数只有当传入的序列中的item是hashable对象时
# 才能工作(本例中是数字)，因为只有hashable对象才能互相比较是否相等
# 名词解释：什么是hashable？
# 如果一个对象在其生命周期内有一个固定不变的哈希值(需要__hash__()方法)且可以与其他对象进行比较操作(需要__eq__()方法)，
# 那么这个对象就是可哈希对象(hashable)，可哈希对象必须有相同的哈希值才算相等。
# Python内置对象中的不可变对象(字符串，数字，元组)都是可哈希对象，Python内置对象中的可变对象(列表，集合，字典)都是不可
# 哈希对象，这里的不可变对于Python内置对象而言是指对象的值不可变，对用户自定义的对象而言是指对象的id不可变，因为id本来就
# 不会发生变化，所以默认用户自定义的对象都是可哈希的。


# 以下这个函数可以对由hashable对象或者非hashable对象组成的队列去重, 这个函数的核心思想其实就是把不能比较的非hashable
# 对象转换成hashable对象来比较
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))

b = [[1, 2, 3], [2, 3, 4], [1, 2, 3], [3, 4, 5]]
print(list(dedupe(b, key=lambda l: (l[0], l[1], l[2]))))

c = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(c)))
