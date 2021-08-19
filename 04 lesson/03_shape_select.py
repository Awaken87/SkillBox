# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

point_0_tri = sd.get_point(200, 200)

def triangle(point, angle=0, line_length=200, color_line=sd.COLOR_CYAN):
    v1 = sd.get_vector(start_point=point_0_tri, angle=angle, length=line_length, width=3)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=line_length, width=3)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=line_length, width=3)
    v1.draw(color=color_line)
    v2.draw(color=color_line)
    v3.draw(color=color_line)

point_0_squ = sd.get_point(200, 200)
def square(point_left_botton=point_0_squ, angle=0, length_line=200, color_squ=sd.COLOR_CYAN):
    v1 = sd.get_vector(start_point=point_0_squ, angle=angle, length=length_line, width=3)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+90, length=length_line, width=3)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle+180, length=length_line, width=3)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle+270, length=length_line, width=3)
    v1.draw(color=color_squ)
    v2.draw(color=color_squ)
    v3.draw(color=color_squ)
    v4.draw(color=color_squ)

point_0_fiv = sd.get_point(200, 150)
def fiveline(point_left_botton=point_0_fiv, angle=0, length_line=200, color_fiv=sd.COLOR_CYAN):
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

point_0_six = sd.get_point(200, 150)
def sixline(point_left_botton=point_0_six, angle=200, length_line=0, color_six=sd.COLOR_CYAN):
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

print('Номера фигур:\n1. Треугольник\n2. Квадрат\n3. Пятигранник\n4. Шестигранник')
figure_num = input('Выберите фигуру и введите еее номер в консоль:')
try:
    figure = int(figure_num)
    if 1 <= figure <= 4:
        if figure == 1:
            triangle(point=point_0_tri, angle=0, line_length=200, color_line=sd.COLOR_RED)
        if figure == 2:
            square(point_left_botton=point_0_squ, angle=0, length_line=200, color_squ=sd.COLOR_RED)
        if figure == 3:
            fiveline(point_left_botton=point_0_fiv, angle=0, length_line=200, color_fiv=sd.COLOR_GREEN)
        if figure == 4:
            sixline(point_left_botton=point_0_six, angle=0, length_line=200, color_six=sd.COLOR_ORANGE)
    else:
        print('Введеный номер вне диапазона')
except ValueError:
    print('Это не число!')


sd.pause()
