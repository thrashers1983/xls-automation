# basketball_star = 'michael jordan'
# quote = f"{basketball_star.title()} says: nothing is impossible unless you didn't afford."
# print(quote)


# favorite_language = ' ruby\n\t'
# print(favorite_language.rstrip())
# print(favorite_language.lstrip())
# print(favorite_language.strip())
# print()
# print('python')

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

usernames = ['John', 'Mary', 'Mike', 'Jack']
lower_usernames = []
for username in usernames:
    lower_usernames.append(username.lower())
print(lower_usernames)



