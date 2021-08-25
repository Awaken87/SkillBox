# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = 1200, 600

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# sd.snowflake(center=point_0, length=200, factor_a=0.5)
list_x = [50,300,500,250,280,400,300,350,500,700,800,1000]
list_y = [500,490,480,485,490,495,500,495,470,480,475,485,490,465,460]
list_length = [random.randrange(1,50,5), random.randrange(1,50,5), random.randrange(1,50,5), random.randrange(1,50,5),
               random.randrange(1,50,5),random.randrange(1,50,5),random.randrange(1,50,5),random.randrange(1,50,5)]
shift_x = random.randrange(0, 50, 1)
shift_x1 = random.randrange(0, 50, 1)
shift_x2 = random.randrange(0, 50, 1)
shift_x3 = random.randrange(0, 50, 1)
shift_x4 = random.randrange(0, 50, 1)
shift_x5 = random.randrange(0, 50, 1)
while True:
    sd.clear_screen()
    point_0 = sd.get_point(list_x[0], list_y[0])
    sd.snowflake(center=point_0, length=list_length[0])
    list_y[0] -= 10
    if list_y[0] < 20:
        break
    list_x[0] = list_x[0] + shift_x

    point_1 = sd.get_point(list_x[1], list_y[1])
    sd.snowflake(center=point_1, length=list_length[1])
    list_y[1] -= 10
    if list_y[1] < 20:
        break
    list_x[1] = list_x[1] + shift_x1

    point_2 = sd.get_point(list_x[2], list_y[2])
    sd.snowflake(center=point_2, length=list_length[2])
    list_y[2] -= 10
    if list_y[2] < 20:
        break
    list_x[2] = list_x[2] + shift_x2

    point_3 = sd.get_point(list_x[3], list_y[3])
    sd.snowflake(center=point_3, length=list_length[3])
    list_y[3] -= 10
    if list_y[3] < 20:
        break
    list_x[3] = list_x[3] + shift_x3

    point_4 = sd.get_point(list_x[4], list_y[4])
    sd.snowflake(center=point_4, length=list_length[4])
    list_y[4] -= 10
    if list_y[4] < 20:
        break
    list_x[4] = list_x[4] + shift_x4

    point_5 = sd.get_point(list_x[5], list_y[5])
    sd.snowflake(center=point_5, length=list_length[5])
    list_y[5] -= 10
    if list_y[5] < 20:
        break
    list_x[5] = list_x[5] + shift_x5

    point_6 = sd.get_point(list_x[6], list_y[6])
    sd.snowflake(center=point_6, length=list_length[6])
    list_y[6] -= 10
    if list_y[6] < 20:
        break
    list_x[6] = list_x[6] + shift_x1

    point_7 = sd.get_point(list_x[7], list_y[7])
    sd.snowflake(center=point_7, length=list_length[7])
    list_y[7] -= 10
    if list_y[7] < 20:
        break
    list_x[7] = list_x[7] + shift_x2

    point_8 = sd.get_point(list_x[8], list_y[8])
    sd.snowflake(center=point_8, length=list_length[2])
    list_y[8] -= 10
    if list_y[8] < 20:
        break
    list_x[8] = list_x[8] + shift_x3
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


