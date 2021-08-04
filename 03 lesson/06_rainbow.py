# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# sd.resolution = (450, 500)
# x = 50 #задаем начальные координаты х
# y = 50 #задаем начальные координаты у
# x_f = 350 #задаем конечные координаты х
# y_f = 450 #задаем конечные координаты у
# for i in range(7):
#     start = sd.get_point(x, y)
#     finish = sd.get_point(x_f, y_f)
#     step = 5 #задаем шаг линий
#     sd.line(start_point=start, end_point=finish, color=rainbow_colors[i], width=4)
#     x += step
#     x_f +=step



# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
sd.resolution = (1000, 600)
point = sd.get_point(500, -100)
radius = 450
for i in range(7):
    radius += 5
    sd.circle(center_position=point, radius=radius, color=rainbow_colors[i], width=8)

sd.pause()
