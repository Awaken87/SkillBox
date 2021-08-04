# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

simple_draw.resolution = (1000, 600)
x_r = 100
y_r = 50
x_l = 0
y_l = 0

for j in range(2):
    for i in range(0, 1001, 100):
        point_1 = simple_draw.get_point(x_l, y_l)
        point_2 = simple_draw.get_point(x_r, y_r)
        simple_draw.rectangle(left_bottom=point_1, right_top=point_2, color=[170, 150, 50], width=2)
        step_horizont = 100
        x_l += step_horizont
        x_r += step_horizont
    x_l = 50
    x_r = 150
    step_vertical = 50
    y_l += step_vertical
    y_r += step_vertical

simple_draw.pause()
