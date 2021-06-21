'''
ЛР13: Уточнение корней

Назначение:
Уточнение корней методом Ридера и сравнение с библиотечной функций из scipy

Переменные:
leftBorder - левая граница отрезка
rightBorder - правая граница отрезка
a - левая граница при уточнении
b - правая граница при уточнении
c - среднинная точка между a и b
fa - значние функции в точке a
fb - значние функции в точке b
fc - значние функции в точке с
iterCount1 - число итераций моей функции
iterCount2 - число итераций функции scipy
time1 - время работы моей функции
time2 - время работы функции scipy
startTime1 - время запуска моей функции
startTime2 - время запуска фукнции scipy
xTol - точность по оси х
yTol - тончость по оси y
maxIter - максимальное число итераций
'''

from time import perf_counter
from math import sin, sqrt, floor, log10, copysign, fabs
import scipy.optimize as sc

errors = [
    "Нет ошибок",
    "Превышено максимальное число итераций",
    "Корень находится на границе отрезка",
    "Деление на 0",
    "Длина отрезка меньше значения точности"
]

def printMainMenu(maxIter, xTol, yTol):
    print('''
    Меню:
    
    1 - Поиск корней
    2 - Изменить максимальное число итераций (установлено {:d})
    3 - Изменить значение точности (установлено {:.0e})
    4 - Изменить уточнение по оси (установлено по {:s})
    5 - Вывести номера ошибок
    
    0 - Выход
'''.format(maxIter, xTol if xTol != None else yTol, 'x' if xTol != None 
else 'y'))


def f(x):
    return sin(x)


def numToStr(x, digit=7):
    if x == 0:
        return '0'
    if abs(x) >= 10**digit:
        return ('{:.'+str(digit-1)+'e}').format(x)
    if abs(x) >= 10**(digit-1):
        return str(int(x))
    if abs(x) < 0.1:
        return ('{:.'+str(digit-1)+'e}').format(x)
    if abs(x) < 1:
        return ('{:.'+str(digit)+'f}').format(x)
    return str(round(x, -floor(log10(abs(x)))-1 + digit))


def formTable(rootNum, a, b, x1, iterCount1, time1, codeError1,
    x2, iterCount2, time2, codeError2, xtol):
    if rootNum == 1:
        if xtol == None:
            print("\nИспользуя функцию из scipy нельзя найти корень с заданной\
точностью по y")

        print("\n{:^14s}{:^6s}{:^10s}{:^10s}{:^16s}{:^9s}{:^9s}{:^12s}{:^6s}"
        .format('', "Номер", '', '', "Значение", "Значение", "Число", "Время", 
        "Код"))
        print("{:^14s}{:^6s}{:^10s}{:^10s}{:^16s}{:^9s}{:^9s}{:^12s}{:^6s}"
        .format("Метод", "корня", "A", "B", "X", "f(X)", 
        "итераций", "работы", "ошибки"))
    
    if codeError1 in (0, 2):
        print("{:<14s}{:^6d}{:^10s}{:^10s}{:^16s}{:^9s}{:^9d}{:>.7f} ms {:^6}"
        .format("Ридера", rootNum, numToStr(a, 3), numToStr(b, 3),
        numToStr(x1, 9), numToStr(f(x1), 1), iterCount1, time1, codeError1))
    else:
        print("{:<14s}{:^6d}{:^10s}{:^10s}{:^16s}{:^9s}{:^9d}{:>.7f} ms {:^6}"
        .format("Ридера", rootNum, numToStr(a, 3), numToStr(b, 3),
        '-', '-', iterCount1, time1, codeError1))
    if xtol != None:
        if codeError2 in (0,2):
            print("{:<14s}{:^6d}{:^10s}{:^10s}{:^16s}{:^9s}{:^9d}{:>.7f} ms {:^6}"
            .format("Ridder(scipy)", rootNum, numToStr(a, 3), numToStr(b, 3),
            numToStr(x2, 9), numToStr(f(x2), 1), iterCount2, time2, codeError2))
        else:
            print("{:<14s}{:^6d}{:^10s}{:^10s}{:^16s}{:^9s}{:^9d}{:>.7f} ms {:^6}"
            .format("Ridder(scipy)", rootNum, numToStr(a, 3), numToStr(b, 3),
            '-', '-', iterCount2, time2, codeError2))


def ridderOwnX(f, x1, x2, xtol = None , ytol = None, maxiter = 10):
    fl = f(x1)
    fh = f(x2)
    if ((fl > 0.0 and fh < 0.0) or (fl < 0.0 and fh > 0.0)):
        xl = x1
        xh = x2
        ans = 10e+8
        for j in range(1, maxiter + 1):
            xm = 0.5 * (xl + xh)
            fm = f(xm)  
            s = sqrt(fm*fm - fl*fh)
            if s == 0:
                return (ans, j, 3)
            xnew = xm + (xm-xl)*copysign(1.0, fl - fh)*fm/s
            if fabs(xnew-ans) <= xtol:
                return (ans, j, 0)
            ans = xnew
            fnew = f(ans)

            if fnew == 0.0:
                return (ans, j, 5)
            if copysign(fm,fnew) != fm:
                xl = xm
                fl = fm
                xh = ans
                fh = fnew
            elif copysign(fl, fnew) != fl:
                xh = ans
                fh = fnew
            elif copysign(fh, fnew) != fh:
                xl = ans
                fl = fnew
            else:
                print("Never get here")

            if fabs(xh - xl) <= xtol:
                return (ans, j, 4)
    else:
        if fl == 0.0:
            return (x1, 0, 2)
        if fh == 0.0:
            return (x2, 0, 2)
    print("Never get here")


def ridderOwnY(f, x1, x2, xtol = None , ytol = None, maxiter = 10):
    fl = f(x1)
    fh = f(x2)
    if ((fl > 0.0 and fh < 0.0) or (fl < 0.0 and fh > 0.0)):
        xl = x1
        xh = x2
        ans = 1000**5
        for j in range(1, maxiter + 1):
            xm = 0.5 * (xl + xh)
            fm = f(xm)
            s = sqrt(fm*fm - fl*fh)
            if s == 0:
                return (ans, j, 3)
            xnew = xm + (xm-xl)*copysign(1.0, fl - fh)*fm/s
            if fabs(f(ans)) <= ytol:
                return (ans, j, 0)
            ans = xnew
            fnew = f(ans)

            if fnew == 0.0:
                return (ans, j, 5)
            if copysign(fm,fnew) != fm:
                xl = xm
                fl = fm
                xh = ans
                fh = fnew
            elif copysign(fl, fnew) != fl:
                xh = ans
                fh = fnew
            elif copysign(fh, fnew) != fh:
                xl = ans
                fl = fnew
            else:
                print("Never get here")

    else:
        if fl == 0.0:
            return (x1, 0, 2)
        if fh == 0.0:
            return (x2, 0, 2)
    print("Never get here")


def rootSearch(f, xTol, yTol, maxIter):
    leftBorder, rightBorder = map(float, input("Введите границы отрезка: ")
    .split())
    h = float(input("Введите шаг разбиения: "))
    a, b = leftBorder, leftBorder + h
    if a < rightBorder and b > rightBorder:
        b = rightBorder
    rootNum = 0
    while a < rightBorder:
        if f(a)*f(b) <= 0:
            rootNum += 1
            
            if xTol != None:
                time1Start = perf_counter()
                myRes = ridderOwnX(
                    f, a, b,
                    xtol = xTol,
                    ytol = yTol,
                    maxiter = maxIter
                    )
                time1 = perf_counter() - time1Start
            else:
                time1Start = perf_counter()
                myRes = ridderOwnY(
                    f, a, b,
                    xtol = xTol,
                    ytol = yTol,
                    maxiter = maxIter
                    )
                time1 = perf_counter() - time1Start

            codeError2 = None
            try:
                time2Start = perf_counter()
                scipyRes = sc.ridder(
                    f, a, b, 
                    xtol = (xTol if xTol != None else yTol), 
                    maxiter = maxIter, 
                    full_output = True
                    )[1]
                time2 = perf_counter() - time2Start
            except ZeroDivisionError:
                codeError2 = 3
            except:
                codeError2 = 6

            if codeError2 == None:
                if scipyRes.root in (a, b):
                    codeError2 = 2
                elif scipyRes.iterations > maxIter:
                    codeError2 = 1
                else:
                    codeError2 = 0


            formTable(rootNum, a, b, 
                myRes[0], myRes[1], time1*1000, myRes[2],
                scipyRes.root, scipyRes.iterations if scipyRes.root not in 
                (a, b) else 0, time2*1000, codeError2, xTol)

        a, b = a + h, b + h
        if a < rightBorder and b > rightBorder:
            b = rightBorder
    
    if rootNum == 0:
        print("\nКорни не найдены")


def main():
    maxIter = 10
    xTol, yTol = 0.001, None
    
    choice = None
    while choice != '0':
        printMainMenu(maxIter, xTol, yTol)
        choice = input("Ваш выбор: "); print()
        if choice == '1':
            rootSearch(f, xTol, yTol, maxIter)
        elif choice == '2':
            maxIter = int(input("Введите новое максимальное число итераций: "))
            print("\nМаксимальное число итераций изменено")
        elif choice == '3':
            if xTol != None:
                xTol = float(input("Введите новое значение точности: "))
            else:
                yTol = float(input("ВведитеC новое значение точности: "))
        elif choice == '4':
            xTol, yTol = yTol, xTol
            print('Уточнение по оси изменено')
        elif choice == '5':
            print('Номера ошибок:')
            for i, line in enumerate(       errors):
                print(i, '-', line)
        elif choice == '0':
            print("Выход")
        else:
            print("Неизвестная команда")

main()
