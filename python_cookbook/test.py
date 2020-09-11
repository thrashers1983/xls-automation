# f = lambda: 'foo'
# print(f())
#
# zidian = {'name': 'IBM', 'shares': 100, 'price': 91.1}
# key = lambda s: s['price']
# print(key(zidian))
#
# a = [(5, 4), (3, 1), (4, 4)]
# a.sort(key=lambda x: x[1])
# print(a)
#
# import heapq
#
# zz = [1, 3, 5, 7, 9]
# print(zz)
# heapq.heappush(zz, 2)
# print(zz)
# print(heapq.heappop(zz))
# print(heapq.heappop(zz))
# print(zz)
# heapq.heappush(zz, 4)
# print(zz)
# print(heapq.heappop(zz))
# print(heapq.heappop(zz))
# print(zz)
# print(type(zz))
# # 以上这个测试可以看出来，对一个列表调用heapq.heappush()，这个列表就具有堆的特性，但是他的类型依然是list
#
#
# def prt(x):
#     return -x
#
#
# result = prt(2)
# print(result)
#
#
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"user {self.name}, it's age is {self.age}"
#
#     def __repr__(self):
#         return f"User('{self.name}', {self.age})"
#
#
# me = User("yiping", 36)
# print(me)
# print(me.__str__())
# print(me.__repr__())
# # 从这里可以看到实例是调用了__str__()方法来返回结果，但是如果没有重构__str__()方法，只重构了__repr__()方法，
# # 则调用__str__()的返回结果和调用__repr__()的返回结果是一样的，所以打印出来是__repr__()的返回值
#
# from datetime import datetime
# now = datetime.now()
# print(now)
# print(now.__str__())
# print(now.__repr__())
# # 从这里可以明显看到__str__()和__repr__()返回的值不一样
#
#
# def shabi(x, key):
#     print(x)
#     print(key(x))
#
#
# shabi(1, key=lambda x: x+1)
