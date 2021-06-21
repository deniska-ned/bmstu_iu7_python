'''
ЛБ4: График фукнции

Назначение:
Построение графика  функции f = x/2*sqrt(x*x+1)-log(x+sqrt(x*x+1))

Переменные:
MAX_LEN_Y - максимальная длина оси OY
start, stop - начальное и конечное значение
step - шаг
serifs - количество засечек
x - значение х
i - переменная цикла
f - значение функции f
fMax - максимальное значение функций
fMin - минимальное значение функций
lenY - длина оси y
s - строка для вывода значений x
sy - строка для вывода графика
j - номер элемента строки для замены на символ функции
zero_axis - длина до х
'''

from math import sin, log, pi, sqrt, floor, log10

MAX_LEN_Y = 79 - 14
zero_axis = None

print('f = x/2*sqrt(x*x+1)-log(x+sqrt(x*x+1))\n')

start, stop, step = map(float, input(
'Введите начальное значение, конечное и шаг: ').split())

#start, stop, step = 0.8, 1.2, 0.1
while not (start <= stop and step > 0):
    if start > stop:
        print("Конечное значение должно быть не меньше начального")
    if step <= 0:
        print("Значение шага должно быть положительным")
    print("Попробуйте еще")
    start, stop, step = map(float, input(
    '\nВведите начальное значение, конечное и шаг: ').split())
#serifs = 5
serifs = int(input('Введите количество засечек: '))
while not (4 <= serifs <= 8):
    print("Допустимое число засечек от 4 до 8\nПопробуйте еще")
    serifs = int(input('\nВведите количество засечек: '))

#Вычисление максимального и минимального значения
x = start
fMax = fMin = x/2*sqrt(x*x+1)-log(x+sqrt(x*x+1))

for i in range(int(start*100), int(stop*100+1), int(step*100)):
    x = i/100

    f = x/2*sqrt(x*x+1)-log(x+sqrt(x*x+1))
    if f > fMax:
        fMax = f
    if f < fMin:
        fMin = f

if fMin == fMax:
    print("\nПри введеных значениях невозможно построить график")
    s = ""
    if fMax == 0:
        s += '{:d}'.format(0)
    elif abs(fMax) >= 100000 or abs(fMax)<=0.01:
        s += "{:<6.0e}".format(fMax)
    else:
        s += "{:<.4f}".format(fMax)
    print("При данных значениях X функции всегда принимают значение {:s}"\
    .format(s))
    
else:
    #Вывод значений над осью
    count_space = (MAX_LEN_Y - serifs)//(serifs-1)
    lenY = count_space * (serifs-1) + serifs
        
    s = '\n' + ' '*9
    for i in range(serifs):
        f = fMin + (fMax-fMin)/(serifs-1)*i
        if abs(fMax) + abs(fMin) > 2 and abs(f)<1:
            zero_axis = len(s) - 10
            s += "{:<6d}".format(0) 
        elif abs(f) >= 100000 or abs(f)<=0.01:
            s += "{:<6.0e}".format(f)
        elif abs(f) > 1:
            s += "{:<6d}".format(int(round(f, -int(floor(log10(abs(f)))) + 1)))
        elif f == 0:
            s += "{:<6d}".format(0)
        else:
            s += "{:<6s}".format(str(round(f, -int(floor(log10(abs(f)))) + 1)))
        if i < serifs - 1:
            s += ' '*(count_space - 6 + 1)
    print(s)

    #Вывод строки с засечками
    s = ' '*4 + 'x' + ' '*4 + ('┴' + '─'*count_space)*(serifs-1) + '┴' + ' y'
    
    if fMin <= 0 <= fMax:
        if zero_axis == None:
            j = int((0-fMin)/(fMax-fMin)*(lenY-1)) + 9
            s = s[:j] + '┬' + s[j+1:]
        else:
            if s[zero_axis + 9] == '┴':
                s = s[:zero_axis + 9] + '┼' + s[zero_axis + 10:]
            else:
                s = s[:zero_axis + 9] + '┬' + s[zero_axis + 10:]
    
    print(s)

    #Вывод графика


    for i in range(int(start*100), int(stop*100+1), int(step*100)):
        x = i/100
        s = '{:8.2f} '.format(x)
        sy = ' '*lenY

        if zero_axis != None:
            sy = sy[:zero_axis] + '│' + sy[zero_axis + 1:]
        elif fMin <= 0 <= fMax:
            j = int((0-fMin)/(fMax-fMin)*(lenY-1))
            sy = sy[:j] + '│' + sy[j + 1:]

        f = x/2*sqrt(x*x+1)-log(x+sqrt(x*x+1))
        j = int((f-fMin)/(fMax-fMin)*(lenY-1))
        sy = sy[:j] + '*' + sy[j + 1:]    
        print(s + sy)
