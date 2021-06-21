#Защита ЛР №4

from math import sin

print("f = sin(x)\n")

start, stop, step = map(float, input('Введите начальное значение, конечное \
и шаг: ').split())

while start >= stop or step <= 0:
    if start == stop:
        print('Начальное и конечное значения должны быть различны')
    if start > stop:
        print('Начальное значение должно быть меньше конечного')
    if step <= 0:
        print('Значение шага должно быть положительным')
    print('Попробуйте еще')
    start, stop, step = map(float, input('\nВведите начальное значение, конечное \
    и шаг: ').split())

#start, stop, step = 0, 6, 0.1

LEN_Y = 61

fmax = fmin = sin(start)

#Подсчет минимального и максимального значения
for i in range(int(start*100), int(stop*100 + 1), int(step*100)):
    x = i / 100
    if sin(x) > fmax:
        fmax = sin(x)
    if sin(x) < fmin:
        fmin = sin(x)

#Вывод значений над графиком
s = ' '*9 + '{:<10.2f}'.format(fmin)+' '*(LEN_Y-20)+'{:>10.2f}'.format(fmax)
print(s)

#Вывод оси y
sl = ' '*7 + 'x' + ' '
sc = '─'*LEN_Y
if fmin <= 0 <= fmax:
    j = round((0 - fmin)/(fmax-fmin)*(LEN_Y - 1))
    sc = sc[:j]+'┬'+sc[j+1:]
sr = ' ' + 'y №'
print(sl+sc+sr)

#Вывод графика
num = 1

for i in range(int(start*100), int(stop*100 + 1), int(step*100)):
    x = i / 100
    sl = '{:8.2f}'.format(x) + ' '
    
    sr = ' '*3 + str(num)
    num += 1

    #формирование оси
    sc = ' '*LEN_Y
    if fmin <= 0 <= fmax:
        j = int((0 - fmin)/(fmax-fmin)*(LEN_Y - 1))
        sc = sc[:j]+'│'+sc[j+1:]

    #вывод значений
    f = sin(x)
    j = round((f - fmin)/(fmax-fmin)*(LEN_Y - 1))
    sc = sc[:j]+'*'+sc[j+1:]
    
    print(sl+sc+sr)
    
