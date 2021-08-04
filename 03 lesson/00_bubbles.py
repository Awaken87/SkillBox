# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(100, 100)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(center_position=point, radius=radius, color=[190,120,180], width=4)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# def buble(center_x, center_y, step):
#     point = sd.get_point(center_x, center_y)
#     radius = 50
#     step_input = step
#     for _ in range(3):
#         radius += step_input
#         sd.circle(center_position=point, radius=radius, color=[190, 120, 180], width=4)
# buble(200, 300, 30)

# Нарисовать 10 пузырьков в ряд
# for i in range(100, 1010, 100):
#     point = sd.get_point(i, 100)
#     radius = 50
#     for _ in range(3):
#         radius += 5
#         sd.circle(center_position=point, radius=radius, color=[190,120,180], width=4)

# Нарисовать три ряда по 10 пузырьков
for i in range(100, 1010, 100):
    point = sd.get_point(i, 100)
    radius = 50
    for _ in range(3):
        radius += 5
        sd.circle(center_position=point, radius=radius, color=[190,120,180], width=4)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()