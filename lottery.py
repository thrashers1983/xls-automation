# from random import randint
#
# red_raw = []
# red_final = []
# blue = []
#
# for i in range(1, 7):
#     red_raw.append(randint(1, 33))
#
# while red_raw:
#     red_ball = red_raw.pop()
#     if red_ball not in red_final:
#         red_final.append(red_ball)
#
# for red_ball in red_raw:
#     if red_ball not in red_final:
#         red_final.append(red_ball)
#
# while len(red_final) < 6:
#     red_add = randint(1, 33)
#     if red_add not in red_final:
#         red_final.append(red_add)
#
# blue.append(randint(1, 16))
#
# red_final.sort()
# print(red_final)
# print(blue)

from random import choice

def two_color_ball():

    red_ball_pool = []
    blue_ball_pool = []
    red_ball_choice = []
    blue_ball_choice = []

    for i in range(1, 34):
        red_ball_pool.append(i)

    for i in range(1, 17):
        blue_ball_pool.append(i)

    for i in range(1, 7):
        red_ball = choice(red_ball_pool)
        red_ball_choice.append(red_ball)
        red_ball_pool.remove(red_ball)

    blue_ball = choice(blue_ball_pool)
    blue_ball_choice.append(blue_ball)
    blue_ball_pool.remove(blue_ball)

    red_ball_choice.sort()
    return(red_ball_choice, blue_ball_choice)

result = two_color_ball()
print(result)

