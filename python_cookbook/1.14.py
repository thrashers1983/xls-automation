# 1.14. Sorting Objects Without Native Comparison Support
# 需求：有一系列User类的实例，想要按照实例的某些属性排序
from operator import attrgetter


class User:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return 'User({0} {1} {2})'.format(self.user_id, self.first_name, self.last_name)


users = [User(23, 'michael', 'jordan'), User(3, 'magic', 'johnson'), User(99, 'charles', 'barkley')]
print(users)
print(sorted(users, key=attrgetter('user_id')))
print(sorted(users, key=attrgetter('last_name', 'first_name')))

# 同样的功能用lambda表达式也可实现，attrgetter()稍微快一点
print(sorted(users, key=lambda u: u.user_id))
print(sorted(users, key=lambda u: (u.last_name, u.first_name)))

# attrgetter()也可以用于min()，max()
print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))




