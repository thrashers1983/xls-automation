# 读取整个文件
with open('data/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
# open()函数返回一个对象代表这个文件pi_digits.txt，然后把这个对象赋给file_object，关键字with的作用是当不再需要访问这个文件的时候关闭该文件，
# 虽然也可以手动用close()函数关闭文件，但通常由于不知道什么时候该关闭文件而导致错误发生，用with的好处是不需要关心什么时候关闭文件，python会在
# with代码块执行完成后自动关闭文件，read()方法读取整个文件内容
#
# read()方法读到文件末尾的时候会返回一个空字符串，表现为一个空行，如果想去掉空行，用rstrip()
print(contents.rstrip())
print()
# 逐行读取，待研究问题：为什么文件对象是可以用for循环迭代的
with open('data/pi_digits.txt') as file_object:
    for line in file_object:
        print(line)
# 读出来的每行间都会有空行，因为文件每行的末尾都有换行符，并且print()本身会带一个换行符，用rstrip()去掉空行
with open('data/pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
print()
# 用readlines()方法逐行读取文件，并返回一个列表
filename = 'data/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
print()
# 对从文件内读出来的内容做处理
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
# 打出来的字符串包含了每行左边的空格，可以用strip()把两边的空白都剥掉
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
# python把读出来的文件内容按字符串处理，可以用int()函数或者float()函数来转换类型
print()
# 题外话，在这里记录一下：对列表可以做的一些操作，比如切片，for循环，查找列表是否含有某元素等等，这些操作对字符串也可以做
#
# 用replace()方法替换字符串
filename = 'data/learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        line = line.replace('python', 'swift')
        print(line.rstrip())
print()
# 写入一个空文件
filename = 'data/programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
# open()的第二个参数'w'告诉python用write mode打开这个文件，其他几个参数值：'r'是read mode, 'a'是append mode，'r+'是读写模式，不写第二
# 个参数默认是read mode，如果这个文件不存在，open()函数会自动创建这个文件，但是如果文件已存在，用'w'模式打开这个文件会先删除文件的内容，再返回
# 一个文件对象内容为空，write()方法不加换行符，如果想要换行，需要手动加换行符
# python只能把字符串写入文本文件，所以如果想要写入数字类型的数据，要先用str()把数据转换成字符串格式
#
# 附加内容到一个文件
with open(filename, 'a') as file_object:
    file_object.write("And I love analysing data.\n")
# 用'a'模式打开一个文件，如果这个文件不存在，python也会自动创建这个文件，如果文件已存在，则是把内容附加到文件末尾
#
# 这是书上的习题
filename1 = 'data/user_visit.txt'
with open(filename1, 'w') as file_object:
    while True:
       name = input('whats your name: ')
       if name == 'q':
           break
       print(f'Hi {name.title()}')
       file_object.write(f'{name.title()} has visited.\n')
print()
# 使用try-except Blocks来应对错误
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
# 如果try代码块能正常执行，则跳过except代码块，如果try出错了，则检查except的错误是否和try的出错匹配，如果匹配则执行except代码块
# 如果try-expect后面还有代码，程序会继续运行
print()
# 如果try block执行成功，则跳至else block
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ValueError:
        print('Enter a number you idiot!')
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
print()
# FileNotFoundError Exception
filename = 'data/alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
# 如果文件的编码和系统默认编码不一样，用encoding参数指定编码，split()方法每遇到一个空格就把字符串分成部分，并返回一个列表包含每个部分
print()
# 把上面这个统计单词数的功能写成一个函数
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filename = 'data/alice.txt'
count_words(filename)
count_words('data/siddhartha.txt')
print()
filenames = ['data/alice.txt', 'data/moby_dick.txt', 'data/siddhartha.txt']
for filename in filenames:
    count_words(filename)
print()
# 有时候在exception发生时不想提供报错信息，就当什么也没发生让程序继续执行
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['data/alice.txt', 'data/moby_dick.txt', 'data/siddhartha.txt']
for filename in filenames:
    count_words(filename)
# pass意思就是什么也不干，pass也视作占位符，先写在这里，以后想起来要做些什么再改
print()
# 这是书上的习题
def find_words(filename, word):
    """Count approximately how many times a word appears in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        num_word = contents.lower().count(word)
        return num_word


c = find_words('data/alice.txt', 'alice')
print(c)
# count()方法返回一个字符串出现的次数
print()
# 把数据存到.json文件中，json文件支持python数据结构，包括字符串列表字典等等
# 用json.dump()把python列表写入一个文件
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'data/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
# json.dump()的两个参数：要写入的数据和文件对象
#
# 用json.load()把列表从文件里读出来
with open(filename) as f:
    numbers = json.load(f)
print(numbers)
print()
# 处理用户数据
filename = 'data/username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
# 先尝试打开username.json，如果文件不存在，说明是第一次运行这个程序，提示用户输入名字并存入username.json，当用户再次运行这个程序时打印问候语
print()
# 把上面处理用户数据这段代码写成函数
def get_stored_username():
    """Get stored username if available."""
    filename = 'data/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'data/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        answer = input(f"{username} is the one who last used the program, are you {username}? y/n ")
        if answer == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
