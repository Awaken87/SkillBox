# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg
point_0 = sd.get_point(200, 200)
#1. Треугольник
# v1 = sd.get_vector(start_point=point_0, angle=0, length=200, width=3)
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=3)
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=200, width=3)
# v1.draw()
# v2.draw()
# v3.draw()

#Треугольник с вызовом из функции
# def triangle(point, angle=0, line_length=0):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=line_length, width=3)
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=line_length, width=3)
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=line_length, width=3)
#     v1.draw()
#     v2.draw()
#     v3.draw()
# triangle(point=point_0, angle=15, line_length=100)

#2. Квадрат
# sd.square(left_bottom=point_0, side=200, width=2,)

#или векторами
# v1 = sd.get_vector(start_point=point_0, angle=0, length=200, width=3)
# v2 = sd.get_vector(start_point=v1.end_point, angle=90, length=200, width=3)
# v3 = sd.get_vector(start_point=v2.end_point, angle=180, length=200, width=3)
# v4 = sd.get_vector(start_point=v3.end_point, angle=270, length=200, width=3)
# v1.draw()
# v2.draw()
# v3.draw()
# v4.draw()

#c функцией
# def square(point_left_botton=point_0, angle=0, length_line=0):
#     v1 = sd.get_vector(start_point=point_0, angle=angle, length=length_line, width=3)
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle+90, length=length_line, width=3)
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle+180, length=length_line, width=3)
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle+270, length=length_line, width=3)
#     v1.draw()
#     v2.draw()
#     v3.draw()
#     v4.draw()
# square(point_left_botton=point_0, angle=10, length_line=150)

#3. Пятиугольник
# v1 = sd.get_vector(start_point=point_0, angle=0, length=200, width=3)
# v2 = sd.get_vector(start_point=v1.end_point, angle=72, length=200, width=3)
# v3 = sd.get_vector(start_point=v2.end_point, angle=144, length=200, width=3)
# v4 = sd.get_vector(start_point=v3.end_point, angle=216, length=200, width=3)
# v5 = sd.get_vector(start_point=v4.end_point, angle=288, length=200, width=3)
# v1.draw()
# v2.draw()
# v3.draw()
# v4.draw()
# v5.draw()

#функция по аналогии

#4. Шестиугольник
# v1 = sd.get_vector(start_point=point_0, angle=0, length=200, width=3)
# v2 = sd.get_vector(start_point=v1.end_point, angle=60, length=200, width=3)
# v3 = sd.get_vector(start_point=v2.end_point, angle=120, length=200, width=3)
# v4 = sd.get_vector(start_point=v3.end_point, angle=180, length=200, width=3)
# v5 = sd.get_vector(start_point=v4.end_point, angle=240, length=200, width=3)
# v6 = sd.get_vector(start_point=v5.end_point, angle=300, length=200, width=3)
# v1.draw()
# v2.draw()
# v3.draw()
# v4.draw()
# v5.draw()
# v6.draw()

#по аналогии

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
