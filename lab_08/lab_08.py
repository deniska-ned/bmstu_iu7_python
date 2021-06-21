from math import log10, floor

'''
ЛБ8: Интегрирование

Назначение:
Подсчет определенного интерала методом трапеций и Weddle
Определение погрешности, интеграла подсчитанного методом трапеций с заданной
точностью относительно ингреграла подсчитанного при помощи первообразной

Переменные:
f_s - строка с функцией
F_s - строка с первообразной функцией
a - начальное значение интервала
b - конечное значение интервала
n - список с числом разбиений
integ - список с подсчитанными интегралами
n_eps - число разбиение при заданной точности
in_tr_0, in_tr_1 - знчения интегралов при подсчете
eps - значение точности
'''

#Метод трапеций
def m_trapeze(a, b, n):
    res = 0
    h = (b-a)/n
    for i in range(1, n):
        res += f(a+h*i)
    res += (f(a)+f(b))/2
    res *= h
    return res

#Метод Weddle
def m_weddle(a, b, n):
    res = 0
    h = (b-a)/n
    for i in range(n//6):
        res += f(a+6*h*i)+5*f(a+h+6*h*i)+f(a+2*h+6*h*i)+6*f(
        a+3*h+6*h*i)+f(a+4*h+6*h*i)+5*f(a+5*h+6*h*i)+f(a+6*h+6*h*i)
    res *= 3*h/10
    return res

#Формирование строки с числом заданной точности
def numToStr(x, digit=7):
    if x == 0:
        return '0'
    if abs(x) >= 10**digit:
        return '{:.5e}'.format(x)
    if abs(x) >= 10**(digit-1):
        return str(int(x))
    if abs(x) < 0.1:
        return ('{:.'+str(digit-1)+'e}').format(x)
    if abs(x) < 1:
        return ('{:.'+str(digit)+'f}').format(x)
    return str(round(x, -floor(log10(abs(x)))-1 + digit))

def f(x):
    return eval(f_s, {'x':x})

#Первообразная функция
def F(x):
    return eval(F_s, {'x':x})    




f_s = input("Введите функцию: ")

a,b = map(float, input("Введите нижнюю и верхнюю границу интегрирования: "
).split())
while b <= a:
    print("Начальное значение должно быть меньше конечного")
    a,b = map(float, input("\nВведите нижнюю и верхнюю границу интегрирования: "
).split())

n = list(map(int, input("Введите 2 количества разбиений: ").split()))
while n[0]%6 or n[1]%6 or n[0]<6 or n[1]<6:
    if n[0]<6 or n[1]<6:
        print("Количество разбиений должно быть положительными")
    if n[0]%6 or n[1]%6:
        print("Количества разбиений должны быть кратны 6")
    n = list(map(int, input("\nВведите 2 количества разбиений: ").split()))

integ = [[0,0],[0,0]]

#Подсчет с заданными числами разбиений
for i in range(len(n)):
    integ[0][i] = m_trapeze(a, b, n[i])    
    integ[1][i] = m_weddle(a, b, n[i])

#Вывод
print('\n{:<14s}  {:>16d}  {:>16d}'.format('Метод', n[0], n[1]))
print('{:<14s}  {:>16s}  {:>16s}'.format('Метод трапеций', 
numToStr(integ[0][0], 9), numToStr(integ[0][1], 9)))
print('{:<14s}  {:>16s}  {:>16s}'.format('Weddle', 
numToStr(integ[1][0],9), numToStr(integ[1][1], 9)))

#Подсчет c заданной точностью
eps = float(input("\nВведите точность: "))

n_eps = 1
in_tr_0 = m_trapeze(a, b, n_eps)

n_eps = 2
in_tr_1 = m_trapeze(a, b, n_eps)

while abs(in_tr_0-in_tr_1)>=eps:
    in_tr_0 = in_tr_1
    n_eps *= 2
    in_tr_1 = m_trapeze(a, b, n_eps)

F_s = input("Введите первообразную функцию: ")

integ_F = abs(F(a) - F(b))

abs_er = abs(integ_F - in_tr_1)
if integ_F == 0:
    rel_er = None
else:
    rel_er = abs_er/abs(integ_F)

#Вывод
print("\nМетод трапеций")
print("Значение интеграла заданной точности:", numToStr(in_tr_1, 9))
print("Число разбиений:", n_eps)

print("\nТочное значение интеграла:", numToStr(integ_F, 9))
print("Абсолютная ошибка:", numToStr(abs_er, 9))
if rel_er == None:
    print("Подсчитать относительную ошибку невозможно")
else:
    print("Относительная ошибка: ", numToStr(rel_er*100, 9), '%', end='')
