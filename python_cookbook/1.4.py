# 1.4. Finding the Largest or Smallest N Items
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)

heapq.heapify(nums)         # 把列表转换成堆
print(nums)                 # 堆的第一个元素永远是堆里最小的(不知道堆的原理，以后再研究)
print(heapq.heappop(nums))
print(nums)                 # 把堆的第一个元素pop掉以后，堆的第二小元素会填补0号位
print(heapq.heappop(nums))
print(nums)

# The most important feature of a heap is that heap[0] is always the smallest item.
# Moreover, subsequent items can be easily found using the heapq.heappop() method, which pops off the
# first item and replaces it with the next smallest item.

# 使用场景：
# 找一个集合的最大值最小值，用max()和min()
# 找一个集合的前N个最大值最小值，而N和集合长度差不太多，用sorted()排序，然后切片
# 找一个集合的前N个最大值最小值，N相比集合长度来说很小，用nlargest()和nsmallest()
