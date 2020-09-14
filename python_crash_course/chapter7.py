# 用input()方法获取用户输入
name = input("Please enter your name: ")
print(f"\nHello, {name}!")
print()
# 如果提示信息很长，可以把提示信息赋给一个变量，再把这个变量传给input()方法
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
print()
# input()方法把获取的用户输入识别为字符串，如果用户输入数字，需要用int()来转成数字格式
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print('Please enter.')
else:
    print('You are not allowed to enter gambling house.')
print()
# 取模运算
print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
print()
# while loop，只要while的条件返回True，循环就一直执行下去
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
print()
# 让用户决定什么时候推出程序
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
print()
# 使用flag来决定循环执行或退出，当有多种情况会导致循环结束，可以用这种方法控制循环
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True       # 定义一个flag变量，只要这个变量=True，则循环继续，直到某个事件发生导致该变量=False，则循环结束
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
print()
# 使用break来退出while循环(break也可以用来退出for循环)
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
print()
# continue跳过后面的代码，回到循环的开头继续执行
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print()
# 避免无限循环：如果不当心写了无限循环，按ctrl+c退出，或者直接退出terminal

# while loop列表和字典
# 把item从一个列表移到另一个列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print()
# 删除列表中重复出现多次的item
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
print()
# 用while loop提示用户输入信息，把用户输入存入字典
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
