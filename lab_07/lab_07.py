"""
ЛР7: Матрицы

Назначение:
    1. Формирование списка по правилу
    W(1) = 0.5
    W(n) = W(n-1), если f(n) = 0
    W(n) = W(n-1) - f(n)*sum(cos(x(k))^2), если f(n) != 0
    n <= 35
    Заменить наибольший элемент на произведение других элементов на нечетных
    позициях (индексация с 1). Вывести наибольший элемент и массив w

    2. Переписать положительные элементы матрицы p(7, 10) в массив X и
    упорядочить их. Вывести вектор X

Переменные:
    ROW_COUNT - число строк матрицы P
    COL_COUNT - число столбцов матрицы P
    choice - выбор элементов меню
    x - список значений x
    f - список значений f
    sum - сумма квадратов косинусов
    i - переменная цикла
    i_max - индекс наибольшего элемета
    multi - произведение нечетных элементов
    p - матрица
    check - переменная проверки ввода
    X - вектор положителных элементов

Тестовый пример:
    Задача 1:
    f = [0, 1, 3, 0]
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    w = [0.5, -7.052, -29.708, -29.708]
    w_max = w[0] = 0.5
    w = [-29.708, -7.052,-29.708, -29.708]

    Задача 2:
    p = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 3, -4, -5, -6, -7, -8, -9, -10],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3]
"""

from math import cos, log10, floor

choice = None

while choice != "0":
    print('''
1 - Первая задача
2 - Вторая задача
0 - Выход
''')
    choice = input("Выбор: ").strip()
    print()
    if choice == "1":
        #Первая задача
        print('''Формирование массива по правилу 
W(1) = 0.5
W(n) = W(n-1), если f(n) = 0
W(n) = W(n-1) - f(n)*sum(cos(x(k))^2), если f(n) != 0
''')
        f = list(map(float, input("Введите в строку список f: ").split()))
        while not 1 < len(f) <= 35:
            print("Длина списка f должна быть от 1 до 35")
            print("Попробуйте еще")
            f = list(map(float, input("\nВведите в строку список f: "
).split()))


        x = list(map(float, input("Введите в строку значения x: "
).split()))
        while not 1 <= len(x) <= 15:
            print("Список X должен быть длиной от 1 до 15")
            print("Попробуйте еще")
            x = list(map(float, input("\nВведите в строку значения x: "
).split()))

        #Формирование массива W
        W = [0.5]

        sum = 0
        for i in x:
            sum += cos(i)**2

        for i in range(1, len(f)):
            if f[i] == 0:
                W.append(W[len(W)-1])
            else:
                W.append(W[len(W)-1]-f[i]*sum)

        #Ввывод сформированного массива W до изменения
        print("\nCозданный массив")
        print("W = [", end='')
        for i in range(len(W)):
            if abs(W[i]) == 0:
                s = '{:}'.format(0)
            elif abs(W[i]) >= 10000000:
                s = '{:.3e}'.format(W[i])
            elif abs(W[i]) >= 1000000:
                s = '{:d}'.format(int(W[i]))
            elif abs(W[i]) < 1:
                s = '{:.6f}'.format(W[i])
            else:
                q = 7 - (1 + floor(log10(abs(W[i]))))
                s = ('{:.'+str(q)+'f}').format(W[i])
            if i != len(W)-1:
                print(s+', ', end='')
            else:
                print(s+']')

        i_max = 0
        for i in range(1, len(W)):
            if W[i] > W[i_max]:
                i_max = i

        #Поиск наибольшего значения
        multi = 1
        for i in range(0, len(W), 2):
            if i != i_max:
                multi *= W[i]
        print('\nЗаменим наибольший элемент на произведение других \
элементов\nна нечетных позициях')
                
        #Вывод наибольшего значения и измененного маассива
        print('\nW_max = W[{:d}] = '.format(i_max), end='')

        if abs(W[i_max]) == 0:
            s = '{:}'.format(0)
        elif abs(W[i_max]) >= 10000000:
            s = '{:.3e}'.format(W[i_max])
        elif abs(W[i_max]) >= 1000000:
            s = '{:d}'.format(int(W[i_max]))
        elif abs(W[i_max]) < 1:
            s = '{:.6f}'.format(W[i_max])
        else:
            q = 7 - (1 + floor(log10(abs(W[i_max]))))
            s = ('{:.'+str(q)+'f}').format(W[i_max])
        print(s)

        W[i_max] = multi
        print("\nРезультат:\nW = [", end='')
        for i in range(len(W)):
            if abs(W[i]) == 0:
                s = '{:}'.format(0)
            elif abs(W[i]) >= 10000000:
                s = '{:.3e}'.format(W[i])
            elif abs(W[i]) >= 1000000:
                s = '{:d}'.format(int(W[i]))
            elif abs(W[i]) < 1:
                s = '{:.6f}'.format(W[i])
            else:
                q = 7 - (1 + floor(log10(abs(W[i]))))
                s = ('{:.'+str(q)+'f}').format(W[i])
            if i != len(W)-1:
                print(s+', ', end='')
            else:
                print(s+']')

    elif choice == "2":
        #Вторая задача

        #Ввод и проверка данных
        P = []
        check = True
        ROW_COUNT = int(input("Введите число строк матрицы: "))
        print("\nВвод исходной матрицы")
        for i in range(ROW_COUNT):
            check = True
            while check:
                check = False
                P.append(list(map(float, input("Введите в строку \
элементы строки №{:d}: ".format(i+1)).split())))
                if i == 0:
                    COL_COUNT = len(P[0])
                if len(P[i]) != COL_COUNT:
                    check = True
                    P.pop()
                    print("Нужно ввести количество элементов "+str(COL_COUNT)+
",попробуйте еще\n")

        #Формирование списка X
        X = []
        for i in range(ROW_COUNT):
            for j in range(COL_COUNT):
                if P[i][j] > 0:
                    X.append(P[i][j])

        #Сортировка по возрастанию
        for i in range(len(X)-1,0,-1):
            j_max = 0
            for j in range(i+1):
                if X[j] > X[j_max]:
                    j_max = j
            X[i], X[j_max] = X[j_max], X[i]
        
        #Вывод
        print("\nВведенная матрица:")
        for i in range(len(P)):
            for j in range(len(P[0])):
                    print(P[i][j],'\t',sep='',end='')
            print()

        print("\nВектор X состоит из отсортированных во возрастанию \
положительных элементов\nматрицы")
        
        if len(X) > 0:
            print("\nX =", X)
        else:
            print("\nВ матрице P нет ни одного положительного элемента")

    elif choice =="0":
        print("Завершение программы")
    else:
        print("Данной команды нет в меню")
