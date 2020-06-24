from random import choice

winning_numbers_red = [2, 5, 6, 18, 21, 33]
winning_numbers_blue = [9]
n = 0

while True:
    my_ticket_red = []
    my_ticket_blue = []
    red_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33]
    blue_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for i in range(1, 7):
        red_ball = choice(red_pool)
        my_ticket_red.append(red_ball)
        red_pool.remove(red_ball)
    blue_ball = choice(blue_pool)
    my_ticket_blue.append(blue_ball)
    blue_pool.remove(blue_ball)

    my_ticket_red.sort()

    if my_ticket_red == winning_numbers_red and my_ticket_blue == winning_numbers_blue:
        print(my_ticket_red)
        print(my_ticket_blue)
        break
    else:
        n += 1
        print(n)






