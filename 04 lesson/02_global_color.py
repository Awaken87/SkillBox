# -*- coding: utf-8 -*-
import random

import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
x_tri = random.randrange(100, 500)
y_tri = random.randrange(100, 500)
point_0_tri = sd.get_point(x_tri, y_tri)

def triangle(point, angle=0, line_length=0, color_line=sd.COLOR_CYAN):
    v1 = sd.get_vector(start_point=point_0_tri, angle=angle, length=line_length, width=3)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=line_length, width=3)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=line_length, width=3)
    v1.draw(color=color_line)
    v2.draw(color=color_line)
    v3.draw(color=color_line)

x_squ = random.randrange(100, 500)
y_squ = random.randrange(100, 500)
point_0_squ = sd.get_point(x_squ, y_squ)
def square(point_left_botton=point_0_squ, angle=0, length_line=0, color_squ=sd.COLOR_CYAN):
    v1 = sd.get_vector(start_point=point_0_squ, angle=angle, length=length_line, width=3)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+90, length=length_line, width=3)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle+180, length=length_line, width=3)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle+270, length=length_line, width=3)
    v1.draw(color=color_squ)
    v2.draw(color=color_squ)
    v3.draw(color=color_squ)
    v4.draw(color=color_squ)

x_fiv = random.randrange(100, 500)
y_fiv = random.randrange(100, 500)
point_0_fiv = sd.get_point(x_fiv, y_fiv)
def fiveline(point_left_botton=point_0_fiv, angle=0, length_line=0, color_fiv=sd.COLOR_CYAN):
    v1 = sd.get_vector(start_point=point_0_fiv, angle=angle, length=length_line, width=3)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+72, length=length_line, width=3)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle+144, length=length_line, width=3)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle+216, length=length_line, width=3)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length_line, width=3)
    v1.draw(color=color_fiv)
    v2.draw(color=color_fiv)
    v3.draw(color=color_fiv)
    v4.draw(color=color_fiv)
    v5.draw(color=color_fiv)

x_six = random.randrange(100, 500)
y_six = random.randrange(100, 500)
point_0_six = sd.get_point(x_six, y_six)
def sixline(point_left_botton=point_0_six, angle=0, length_line=0, color_six=sd.COLOR_CYAN):
    v1 = sd.get_vector(start_point=point_0_six, angle=angle, length=length_line, width=3)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+60, length=length_line, width=3)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle+120, length=length_line, width=3)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle+180, length=length_line, width=3)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length_line, width=3)
    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 301, length=length_line, width=3)
    v1.draw(color=color_six)
    v2.draw(color=color_six)
    v3.draw(color=color_six)
    v4.draw(color=color_six)
    v5.draw(color=color_six)
    v6.draw(color=color_six)

print('Номера цветов:\n1. Красный\n2. Ораньжевый\n3. Желтый\n4. Зеленый\n5. Голубой\n6. Синий\n7. Феолетовый')
color_num=input('Выберите цвет и введите его номер в консоль:')
try:
    color = int(color_num)
    if 1 <= color <= 7:
        if color == 1:
            color = sd.COLOR_RED
        if color == 2:
            color = sd.COLOR_ORANGE
        if color == 3:
            color = sd.COLOR_YELLOW
        if color == 4:
            color = sd.COLOR_GREEN
        if color == 5:
            color = sd.COLOR_CYAN
        if color == 6:
            color = sd.COLOR_BLUE
        if color == 7:
            color = sd.COLOR_PURPLE
        triangle(point=point_0_tri, angle=0, line_length=200, color_line=color)
        square(point_left_botton=point_0_squ, angle=10, length_line=150, color_squ=color)
        fiveline(point_left_botton=point_0_fiv, angle=25, length_line=80, color_fiv=color)
        sixline(point_left_botton=point_0_six, angle=45, length_line=120, color_six=color)
    else:
        print('Введеный номер вне диапазона')
except ValueError:
    print('Это не число!')


sd.pause()
