# 1.2. Unpacking Elements from Iterables of Arbitrary Length
user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record           # 这里的phone_numbers变量总是一个列表，如果没有元素就是空列表
print(name)
print(email)
print(*phone_numbers)
print(phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(*trailing)
print(trailing)
print(current)

records = [
('foo', 1, 2),
('bar', 'hello'),
('foo', 3, 4), ]

def do_foo(*para):
    print('foo', *para)
    print('foo', para)

def do_bar(*para):
    print('bar', *para)

for tag, *args in records:
    if tag == 'foo':
        print(*args)
        print(args)
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
print(fields)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

digits = [1, 10, 7, 4, 5, 9]
results = sum(digits)
print(results)