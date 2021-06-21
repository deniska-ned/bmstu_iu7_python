from math import sqrt

xA, yA = map(float, input('Введите координаты точки A: ').split())
xB, yB = map(float, input('Введите координаты точки B: ').split())
xC, yC = map(float, input('Введите координаты точки C: ').split())
x0, y0 = map(float, input('Введите координаты четвертой точки: ').split())

rAB, rBC, rAC = 0, 0, 0

check1 = (xA - x0)*(yB - yA) - (yA - y0)*(xB - xA)
check2 = (xB - x0)*(yC - yB) - (yB - y0)*(xC - xB)
check3 = (xC - x0)*(yA - yC) - (yC - y0)*(xA - xC)

if (check1 >= 0 and check2 >= 0 and check3 >= 0) or \
(check1 <= 0 and check2 <= 0 and check3 <= 0):
    if xA == xB:
        rAB = abs(x0-xA)
    else:
        k = (yB-yA)/(xB-xA)
        b = yA - k*xA
        rAB = abs(y0-k*x0-b)/sqrt(1+k*k)

    if xB == xC:
        rBC = abs(x0-xB)
    else:
        k = (yC-yB)/(xC-xB)
        b = yB - k*xB
        rBC = abs(y0-k*x0-b)/sqrt(1+k*k)

    if xA == xC:
        rAB = abs(x0 - xC)
    else:
        k = (yC-yA)/(xC-xA)
        b = yC - k*xC
        rAC = abs(y0-k*x0-b)/sqrt(1+k*k)

    if rAB >= rBC and rAB >= rAC:
        print('\nНаиболее удалена сторона AB\nРастояние: {:.4f}'.format(rAB))
    elif rBC >= rAB and rBC >= rAC:
        print('\nНаиболее удалена сторона BC\nРастояние: {:.4f}'.format(rBC))
    else:
        print('\nНаиболее удалена сторона AC\nРастояние: {:.4f}'.format(rAC))
else:
    print('Точка лежит вне треугольника')
