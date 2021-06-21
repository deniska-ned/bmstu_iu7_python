'''
ЛБ4: График значения фукнций

Назначение: Построение графиков  функций f1 = x*sin(log(x)-pi/4)
f2 = x/2*sqrt(x*x+1)-log(x+sqrt(x*x+1))

Переменные:
MAX_LEN_Y - максимальная длина оси OY
start, stop - начальное и конечное значение
step - шаг
serifs - количество засечек
x - значение х
i - переменная цикла
f1 - значение функции f1
f2 - значение функции f2
fMax - максимальное значение функций
fMin - минимальное значение функций
lenY - длина оси y
s - строка для вывода значений x
sy - строка для вывода графика
j - номер элемента строки для замены на символ функции

'┴' '│' '└' '─' '┘' '┼'
'''

from math import sin, log, pi, sqrt, floor, log10

MAX_LEN_Y = 79 - 14

print('\nf1[*] = x*sin(log(x)-pi/4)')
print('f2[#] = x/2*sqrt(x*x+1)-log(x+sqrt(x*x+1))\n')

start, stop, step = map(float, input(
'Введите начальное значение, конечное и шаг: ').split())
while not (start <= stop and step > 0):
    if start > stop:
        print("Конечное значение должно быть не меньше начального")
    if step <= 0:
        print("Значение шага должно быть положительным")
    print("Попробуйте еще")
    start, stop, step = map(float, input(
    '\nВведите начальное значение, конечное и шаг: ').split())

serifs = int(input('Введите количество засечек: '))
while not (4 <= serifs <= 8):
    print("Допустимое число засечек от 4 до 8\nПопробуйте еще")
    serifs = int(input('\nВведите количество засечек: '))

#Вычисление максимального и минимального значения
x = start
fMax = fMin = x/2*sqrt(x*x+1)-log(x+sqrt(x*x+1))

for i in range(int(start*100), int(stop*100+1), int(step*100)):
    x = i/100

    if x > 0:
        f1 = x*sin(log(x)-pi/4)
        if f1 > fMax:
            fMax = f1
        if f1 < fMin:
            fMin = f1
    
    f2 = x/2*sqrt(x*x+1)-log(x+sqrt(x*x+1))
    if f2 > fMax:
        fMax = f2
    if f2 < fMin:
        fMin = f2

if fMin == fMax:
    print("\nПри введеных значениях невозможно построить график")
    s = ""
    if fMax == 0:
        s += '0'
    elif abs(fMax) >= 100000 or abs(fMax)<=0.01:
        s += "{:<6.0e}".format(fMax)
    else:
        s += "{:<.4f}".format(fMax)
    print("При данных значениях X функции всегда принимают значение {:s}"\
    .format(s))
else:
    #Вывод значений над осью
    count_space = (MAX_LEN_Y - serifs)//(serifs-1)

    s = '\n' + ' '*7+'y '
    for i in range(serifs):
        f = fMin + (fMax-fMin)/(serifs-1)*i
        if abs(fMax) + abs(fMin) > 2 and abs(f)<1:
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
    s = ' '*4 + 'x' + ' '*4 + ('┴' + '─'*count_space)*(serifs-1) + '┴'
    print(s)

    #Вывод графика
    lenY = count_space * (serifs-1) + serifs


    for i in range(int(start*100), int(stop*100+1), int(step*100)):
        x = i/100
        s = '{:8.2f} '.format(x)
        sy = ' '*lenY

        if fMin <= 0 <= fMax:
            j = int((0-fMin)/(fMax-fMin)*(lenY-1))
            sy = sy[:j] + '│' + sy[j + 1:]

        if x > 0:
            f1 = x*sin(log(x)-pi/4)
            j = int((f1-fMin)/(fMax-fMin)*(lenY-1))
            sy = sy[:j] + '*' + sy[j + 1:]

        f2 = x/2*sqrt(x*x+1)-log(x+sqrt(x*x+1))
        j = int((f2-fMin)/(fMax-fMin)*(lenY-1))
        if sy[j] == '*':
            sy = sy[:j] + 'X' + sy[j + 1:]    
        else:
            sy = sy[:j] + '#' + sy[j + 1:]
        print(s + sy)
