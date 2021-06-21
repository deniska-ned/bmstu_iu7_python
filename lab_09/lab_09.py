'''
ЛР9: Множества и текстовые файлы

Назначение:
1. Дан текстовый файл R. Создать новый файл Gf, в который записать строки
исходного файла в обратном порядке. Массивов и методов read и readlines не
использовать.
2. Задано целое симло M. Найти цифры, которые встречаются в этом числе
более одного раза. Использовать множества.
Многоступенчатых циклов не использовать. Также не использоввать массивы,
строки, файлы, подпрограммы.

Переменные:
'''

choise = None

while choise != '0':
    print('''
1 - Перезапись текстового файла
2 - Поиск повторяющихся цифр

0 - Выход
''')
    choise = input("Введите номер: ")
    if choise == '1':
        #Первая задача
        try:
            R = open('R.txt','r')
            Gf = open('Gf.txt','w')
        except FileNotFoundError:
            print('\nВ директории нет файла')
        except:
            print('Неизвестная ошибка')
        else:
            #Подсчет строк файла
            lineCount = 0
            for i in R:
                lineCount += 1
            R.close()
            
            #Перезапись
            for i in range(lineCount):
                R = open('R.txt','r')
                for j in range(lineCount-i):
                    s = R.readline()
                if i == 0:
                    s += '\n'
                Gf.write(s)
                R.close()
            print('\nПерезапись строк в обратном порядке выполнена')
        finally:
            R.close()
            Gf.close()
    elif choise == '2':
        #Вторая задача
        M = int(input('\nВведите число: '))
        allDigit = set()
        notAllDigit = set()
        m = abs(M)
        while m > 0:
            digit = m%10
            if digit in allDigit:
                notAllDigit.add(digit)
            else:
                allDigit.add(digit)
            m //= 10
        if len(notAllDigit) != 0:
            print('\nПовторяющиеся цифры: ', end='')
            for i in notAllDigit:
                print(i, end='  ')
            print()
        else:
            print('В введенном числе нет подторяющихся цифр')
    elif choise == '0':
        print('\nВыход')
    else:
        print('\nДанного номера нет в меню')
