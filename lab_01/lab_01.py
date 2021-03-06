'''
ЛБ1: Параметры шарового сегмента

Назначение:
Вычисление объема и площади поверхности шарового сегмента через
радиус и высоту

Переменные:
r - радиус сферы
h - высота шарового сегмента
S - площадь шарогово сегмента
V - объем шарового сегмента

Тестовый пример:
r = 5
h = 1
S = 31.4159
V = 14.6608
'''

#импортиование из модуля math числа pi
from math import pi

#Ввод и проверка, что введенные данные лежат в допустимом диапозоне
r = float(input('Введите радиус шара: '))
while r <= 0:
    print('Радиус должен быть больше нуля')
    r = float(input('Введите радиус шара: '))

h = float(input('Введите высоту шарового сегмента: '))
while not 0 < h < r:
    print('Высота должна быть больше нуля и меньше радиуса')
    h = float(input('Введите высоту шарового сегмента: '))

#Подсчет площади шарового сегмента
S = 2*pi*r*h
#Подсчет объема шарового сегмента
V = pi*h*h*(r - h/3)

#Вывод значений
print('\nПри радиусе {} и высоте {}'.format(r, h))
print('Площадь шарового сегмента: {:.4f}'.format(S))
print('Объем шарового сегмента: {:9.4f}'.format(V))
