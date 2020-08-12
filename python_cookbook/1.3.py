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
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print('*'*10)
            print(line, end='')
            print('-' * 20)

q = deque(maxlen=3)     # 创建一个固定长度的队列
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

q = deque()             # 创建一个没有边界的队列
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
