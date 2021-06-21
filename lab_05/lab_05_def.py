from math import floor, log10

print('s = x+x^3/(2*3)-3*x^5/(2*4*5)+3*5*x^7/(2*4*6*7)-3*5*7*x^9/\
(2*4*6*8*9)+...')

x = float(input('\nВведите значение аргумента x: '))
while x==0:
    print('X не может быть равен нулю\nПопробуйте еще')
    x = float(input('\nВведите значение аргумента x: '))

eps = float(input('Введите значение точности: '))
while eps <= 0:
    print('Значение точности должно быть положительным')
    print('Попробуйте еще')
    eps = float(input('\nВведите значение точности: '))

m = int(input('Введите максимальное число итераций: '))
while m <= 0:
    print('Максимальное число итераций должно быть положительм')
    print('Попробуйте еще')
    m = int(input('\nВведите максимальное число итераций: '))

n_start = int(input('Введите номер первого члена ряда для вывода: '))
while n_start <= 0 and n_start>m:
    if n_start < 0:
        print('Номер первого члена для вывода должен быть положительм')
    if n_start > m:
        print('Номер первого члена для вывода должен быть меньше \n\
макисмального числа итераций')
        print('Попробуйте еще')
    n_start = int(input('\nВведите номер первого члена ряда для вывода: '))

step = int(input('Введите значение шага: '))
while step<=0:
    print('Значение шага должно быть положительным')
    print('Попробуйте еще')
    step=int(input('\nВведите значение шага: '))

n_start -=1

item = x
s = item
n = 0
print()
while n <= (m - 1) and abs(item) >= eps:
    if (n-n_start)%step==0:
        if n == n_start:
            print('{:16s} {:s}'.format('Число','Сумма'))
            print('{:16s} {:s}'.format('просуммированных','ряда'))
            print('{:16s} {:s}'.format('членов',''))
        if s == 0:
            string = 'n = {:<12 s = ()}'.format(n+1, 0)
        if abs(s) >= 10000000:
            string = 'n = {:<12} s = {:<10.3e}'.format(n+1, s)
        elif abs(s) >= 1000000:
            string = 'n = {:<12} s = {:<10d}'.format(n+1, int(s))
        elif abs(s) >= 1:
            string = ('n = {:<12} s = {:<10.'+str(7-1-floor(
log10(abs(s))))+'f}').format(n+1, s)
        else:
            string = 'n = {:<12} s = {:.3e}'.format(n+1, s)
        print(string)
    n += 1
    item = - item * x*x*(2*n-1)**2/(2*n*(2*n+1))
    if n == 1:
        item *= -1
    s += item

print()
if n > m-1:
    print('Ряд не сошел за количество циклов {}'.format(m))
else:
    if abs(s) >= 10000000:
        string = 'Номер последнего члена ряда: {:<5}\
\nСумма ряда: {:<10.3e}'.format(n+1, s)
    elif abs(s) >= 1000000:
        string = 'Номер последнего члена ряда: {:<5}\
\nСумма ряда: {:<10d}'.format(n+1, int(s))
    elif abs(s) >= 1:
        string = ('Номер последнего члена ряда: {:<5}\
\nСумма ряда: {:<10.'+str(7-1-floor(log10(s)))+'f}').format(n+1, s)
    else:
        string = 'Номер последнего члена ряда: {:<5}\
\nСумма ряда: {:.3e}'.format(n+1, s)
    print(string)
