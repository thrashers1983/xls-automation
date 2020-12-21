# 1.3. Keeping the Last N Items
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('../data/cookbook_1.3') as f:
        for line, prev_lines in search(f, 'python', 5):
            for pline in prev_lines:
                print(pline, end='')
            print('*'*10)
            print(line, end='')
            print('-' * 20)
# 第一次外层for循环，开始执行search()，由于search()实际上是一个生成器，运行过程中碰到yield返回了line，previous_lines后就停下来了，
# 接下来执行内层for循环，然后开始第二次外层for循环，同样由于search()是生成器的原因，他不会从头开始执行，而是从第一次停下来的地方，也就是
# yield后面那一行继续执行，直到再次碰到yield停下来，吐出两个对象，周而复始直到search()里的for循环读完lines里的内容，那这个生成器就结束了，
# 生成器结束了就不再吐东西出来了，for line, prev_lines拿不到东西也就循环结束了

q = deque(maxlen=3)     # 创建一个固定长度为3的空队列
print(q)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)
for i in q:             # 队列也是可迭代对象
    print(i)

q = deque()             # 创建一个没有边界的空队列
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)

# 这个小节最后的一段话：
# Adding or popping items from either end of a queue has O(1) complexity. This is unlike a list where
# inserting or removing items from the front of the list is O(N).
# 术语解释：O(1)意思是消耗恒定的时间，不管集合中有多少数据，O(N)意思是消耗的时间和集合中的数据量成线性关系
