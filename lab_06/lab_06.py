'''
ЛБ6: Работа со списками

Назначние:
1. Выбор случаным образом неповторяющихся элементов списка
2. Вставка элемента в упорядоченный массив

Переменные:
choice - выбор элемента меню
a - список для обработки
check - переменная для проверки введенных данных
l - конечное число элементов 1ой задачи
r - значение для вставики в массив второй задачи
i - переменная цикла
left - левая граница интервала 
right - правая граница интервала
middle - срединный элемент интевала

Тестовый пример:
Задача 2
a = 1 4 6 9 156
r = 45
Результат: 1 4 6 9 45 156
'''

from random import randint

choise = None

while choise != '0':
    print(
'''

1 - Выбор случаным образом неповторяющихся элементов списка
2 - Вставка элемента в упорядоченный массив
0 - Выход
''')
    choise = input("Выбор: ")
    if choise == "0":
        print('Выход')
    elif choise == "1":
        #Ввод и проверка
        a = list(map(float, input("\nВведите элементы массива в строчку: "
).split()))
        check = False
        check160 = False
        for i in a:
            if a.count(i) > 1:
                check = True
            if  not 0 <= i <= 60:
                check = True
                check160 = True
        if len(a) <= 2 or len(a) > 30:
            check = True
        while check:
            if check160:
                print("Числа должны лежать в диапазоне от 1 до 60")
            elif len(a) <= 2 or len(a) > 30:
                print("Число элеметов списка дожно быть больше 2х\
и не больше 30")
            else:
                print("В списке не могут повторяться элементы")
            print("Попробуйте ещё")
            a = list(map(float, input("\nВведите элементы массива в строчку: "
).split()))
            check,check160 = False, False
            for i in a:
                if a.count(i) > 1:
                    check = True
                if  not 0 <= i <= 60:
                    check = True
                    check160 = True
            if len(a) <= 1:
                check = True
        l = int(input("Введите конечное число элементов массива: "))
        while not 1 < l < len(a):
            print('Возможные значения конечной длины массива: от 2 до',
len(a) - 1)
            print("Попробуйте еще")
            l = int(input("\nВведите конечное число элементов массива: "))
        
        #Удаление элементов
        for i in range(len(a)-l):
            j = randint(0, len(a)-1)
            a.remove(a[j])

        print("\nПолученный список: ")
        for i in a:
            print(i, end=' ')
    elif choise == "2":
        #Ввод и проверка
        a = list(map(float, input("\nВведите упорядоченный список в строку: ")\
.split()))
        check = False
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                check = True
        if len(a) > 16:
            check = True
        while check:
            if len(a) > 16:
                print("Число элементов списка должно быть не больше 15\n\
Попробуйте ещё")
            else:
                print("Введенный список не является неубывающем\nПопробуйте \
ещё")
            a = list(map(float, input("\nВведите упорядоченный список в \
строку: ").split()))
            check = False
            for i in range(len(a) - 1):
                if a[i] > a[i+1]:
                    check = True
        
        r = float(input("Введите число для вставки в массив: "))

        #Поиск нужной позиции бинарным поиском
        left = 0
        right = len(a)-1
        while left != right:
            middle = (left+right)//2
            if r > a[middle]:
                left = middle+1
            else:
                right = middle
        if r>a[len(a)-1]:
            left +=1
        a.insert(left, r)
        print("\nРезультат:")
        for i in a:
            print(i, end=' ')
    else:
        print("Введенного номера нет в меню")
