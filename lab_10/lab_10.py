'''
ЛР№10: Файлы 2

Назначение:
Написать процедуру Sorting для сортировки типизированного файла P методом
"пузырька". Написать также процедуру Data для ввода L, L<=6 элементов файла.
Для печати файла написать процедуру Pokaz. Использовать ее для печати исходного
и преобразованного файлов. В основной программе имя файла целых чисел Z.
Массивов не использовать
'''


FILENAME = 'P.txt'
FILECOPYNAME = 'copy.txt'

def nDelete(s):
    while s!='' and s[len(s)-1]=='\n':
        s = s[:len(s)-1]
    return s.strip()

def copy():
    with open(FILECOPYNAME, 'w') as c:
        with open(FILENAME, 'r') as f:
            for line in f:
                c.write(line)

def getLine(n):
    f = open(FILENAME, 'r')
    for i in range(n+1):
        s = f.readline()
    f.close()
    return nDelete(s)

def swap(i1, i2):
    if i1 != i2:
        if i1 > i2:
            i1, i2 = i2, i1
        #Copy header
        c = open(FILECOPYNAME)
        f = open(FILENAME, 'w')
        for i in range(i1):
            f.write(c.readline())

        #Copy index2
        for line in range(i2-i1+1):
            s = c.readline()
        f.write(s)
        c.close()
        
        #Copy between indexes
        c = open(FILECOPYNAME, 'r')
        for i in range(i1+1):
            s = c.readline()
        for i in range(i2-i1-1):
            f.write(c.readline())
        c.close()

        #Copy index1
        c = open(FILECOPYNAME, 'r')
        for i in range(i1+1):
            s = c.readline()
        f.write(s)
        c.close()

        #Copy footer
        c = open(FILECOPYNAME, 'r')
        i = 0
        for line in c:
            if i > i2:
                f.write(line)
            i += 1
        c.close()
        f.close()
        copy()
                
def Sorting():
    copy()
    lineCount = 0
    with open(FILENAME, 'r') as f:
        for i in f:
            lineCount += 1
    for i in range(lineCount-1, 0, -1):
        for j in range(i):
            if int(getLine(j)) > int(getLine(j+1)):
                swap(j, j+1)
    print("\nСортировка выполнена успешно")
    Pokaz()

def Data():
    L = int(input("\nВведите количество чисел для дозаписи: "))
    while not 0 <= L <= 6:
        print("Допустимое количство должно быть от 0 до 6")
        L = int(input("\nВведите количество чисел для дозаписи: "))
    with open(FILENAME, 'a') as f:
        for i in range(L):
            f.write(input('Введите число №{:d}: '.format(i+1))+'\n')
    Pokaz()
        
def Pokaz():
    fileEmpty = True
    with open(FILENAME) as f:
        if f.readline() != '':
            fileEmpty = False
    if not fileEmpty:
        print('\nСодержимое файла:')
        with open(FILENAME) as f:
            for i in f:
                print(i, end='')
        print()
    else:
        print('\nФайл пуст')

def fileClear():
    with open(FILENAME, 'w') as f:
        f.close()
    copy()
    print('\nФайл очистен')

def main():
    try:
        P = open('P.txt','r')
        P.close()
    except FileNotFoundError:
        print('Файл не найден')
    except Exception as ex:
        print('Неизвестная ошибка:', ex)
    else:
        choice = None
        while choice !='0':
            print('''
Меню
1 - Сортировка
2 - Добавление чисел
3 - Вывод файла
4 - Очистить файл

0 - Выход
''')
            choice = input('Выбор: ').strip()
            if choice == '1':
                Sorting()
            elif choice == '2':
                Data()
            elif choice == '3':
                Pokaz()
            elif choice == '4':
                fileClear()
            elif choice == '0':
                print('\nВыход')
                
            else:
                print('Данного номера нет в меню')
main()
