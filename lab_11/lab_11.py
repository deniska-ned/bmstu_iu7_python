"""
ЛР11: Записи

Назначение:
    Написать программу для работы с записями одинаковой структуры в текстовом
    файле
    Меню:
        Выбор файла
        Создание нового набора записей
        Добавление записей
        Вывод всех записей
        Поиск по одному полю
        Поиск по двум полям
    Записи хранить в одной строке. В записи 3-4 поля, разделенные проблами
"""

menu = """
МЕНЮ:
1 - Выбор файла
2 - Создание нового набора записей
3 - Добавление записей
4 - Вывод всех записей
5 - Поиск по одному полю
6 - Поиск по двум полям
7 - Поиск по времени

0 - Выход
"""


def fileSelection():
    while True:
        fileName = input("\nВведите имя файла: ")
        try:
            file = open(fileName)
            file.close()
        except FileNotFoundError:
            print("Файл не найден")
            choiceCreate = None
            while choiceCreate not in ["y", "n"]:
                choiceCreate = input("Создать его?[y/n]  ")
            if choiceCreate == "y":
                try:
                    file = open(fileName, "x")
                    file.close()
                except Exception as exp:
                    print("Не удалось создать файл")
                    print("Ошибка: " + exp)
                else:
                    print("Файл {:s} создан".format(fileName))
                    break
            else:
                print("Файл не создан")
        else:
            print("Файл {:s} выбран".format(fileName))
            break
    return fileName


def newSet(fileName):
    file = open(fileName, "w")
    file.close()
    addRecords(fileName)


def checkRecord(record):
    if record == None or record.count(" ") != 2:
        if record != None:
            print("\nВ записи должно быть 3 поля")
        return False
    if record == "":
        print("\nВведена пустая строка")
        return False

    record = record.split()
    if not (record[0] + record[1]).isalpha():
        print("\nПервые 2 поля должны состоять из букв")
        return False
    if len(record[2]) != 5 or record[2][2] != ":":
        print(
            "Т\nретье поле - время. Должно состоять из 2х двузначных " +
            "чисел разделенных двоеточием"
        )
        return False
    return True


def addRecords(fileName):
    with open(fileName, "a") as file:
        recordsCount = int(input("\nВведите число новых записей: "))
        while recordsCount < 0:
            print("Количество записей должно быть неотрицательным")
            recordsCount = int(input("\nВведите число новых записей: "))
        for i in range(recordsCount):
            newRecord = (
                        input("Введите запись №{:d}: ".format(i + 1))
                        .strip()
                        .replace("  ", " ")
                        )
            while not checkRecord(newRecord):
                print("Пример корректной записи:\nМосква Прага 20:21")
                newRecord = (
                    input("Введите запись №{:d}: ".format(i + 1))
                    .strip()
                    .replace("  ", " ")
                )
            file.write(newRecord + "\n")
    printFile(fileName)


def printFile(fileName):
    with open(fileName) as file:
        firstLine = file.readline()
    if firstLine == "":
        print("\nФайл пуст")
    else:
        print("\nСодержимое файла:")
        with open(fileName) as file:
            for line in file:
                print(line, end="")


def searchOneSpace(fileName):
    searchSpace = input("Введите значение для поиска: ")
    isFound = False
    with open(fileName) as file:
        for record in file:
            if searchSpace in record:
                isFound = True
                break
    if isFound:
        print("\nНайденные совпадения: ")
        with open(fileName) as file:
            for record in file:
                if searchSpace in record:
                    print(record, end="")
    else:
        print("\nСовпадения не найдены")


def searchTwoSpace(fileName):
    searchSpace1, searchSpace2 = input("Введите 2 значения для поиска: "
    ).split()
    isFound = False
    with open(fileName) as file:
        for record in file:
            if searchSpace1 in record and searchSpace2 in record:
                isFound = True
                break
    if isFound:
        print("\nНайденные совпадения: ")
        with open(fileName) as file:
            for record in file:
                if searchSpace1 in record and searchSpace2 in record:
                    print(record, end="")
    else:
        print("Совпадения не найдены")


def timeStrToInt(s):
    return int(s[:2])*60 + int(s[3:])


def nDelete(s):
    while s != '' and s[-1]=='\n':
        s = s[:len(s)-1]
    return s


def getSpace(record, i):
    return ((nDelete(record)).split())[i]


def searchTime(fileName):
    timeStart, timeEnd = map(timeStrToInt,
    input("Введите диапозон времени: ").split())
    while timeStart > timeEnd:
        print("Начальное значние должно быть не больше конечного")
        timeStart, timeEnd = map(timeStrToInt,
        input("\nВведите диапозон времени: ").split())
    eh = []
    with open(fileName) as file:
        for record in file:
            if timeStart <= timeStrToInt(getSpace(record,2)) <= timeEnd:
                    eh.append(nDelete(record))
    eh.sort(key=lambda x: timeStrToInt(getSpace(x, 2)))
    if eh == []:
        print("\nВылеты не найдены")
    else:
        print("\nНайденные вылеты:")
        for record in eh:
            print(record)


def main():
    fileName = fileSelection()
    choice = None
    while choice != "0":
        print(menu)
        choice = input("Ваш выбор: ")
        if choice == "1":
            fileName = fileSelection()
        elif choice == "2":
            newSet(fileName)
        elif choice == "3":
            addRecords(fileName)
        elif choice == "4":
            printFile(fileName)
        elif choice == "5":
            searchOneSpace(fileName)
        elif choice == "6":
            searchTwoSpace(fileName)
        elif choice == "7":
            searchTime(fileName)
        elif choice == "0":
            print("\nВыход")
        else:
            print("Данного номера нет в меню")


main()
