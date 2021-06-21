'''
ЛБ12: Редактирование текста

Назначение:
Дать пользователю возможность редактировать текст при помощи меню

Переменные и их обозначения:
TEXT - начальный текст
text - список из строк начального текста
choice - переменная выбора элемента меню
align - тип выравнивания
i - переменная цикла
line - линия, элемент списка text
res - строка формирования результата функции
s - строка
sub - подстрока
sep - строка, по которое происходит разбиение строки
old - страрое сначение для замены
new - новое значение для замены
'''


menu = '''
Меню:

1 - Выравнивание по ширине
2 - Выравнивание по левому краю
3 - Выравнивания по правому краю
4 - Замена во все тексте одного слова другим
5 - Удаление заданного слова из текста
6 - Замена арифметических выражений, состоящих из сложения и вычитания
на рузультат их вычисления
7 - Индивидуальное задание 1: Вывод самой короткой строки столбцами (сдано)
8 - Индивидуальное задание 2: Вывод предложений с наибольшим и наименьшим
количеством согласных букв

0 - Выход
'''


TEXT = '''В дверной глазок — в замочную щель. Гениальные
мыслишки — мировые войнушки. Неофициальные
пупы земли. Эмалированные
части головных системю. Инстинктивные 2+8-8
добровольцы во имя вселенной и хлебной корочки. Люди
с большой буквы,
Слово -4 «люди» пишется с большой буквы.'''



digitOper = '012345789+-.'
sogLet = 'бвгджзйклмнпрстфхцчшщъь'


def write(text):
    print('\nТекст: ')
    for line in text:
        print(line)


def isalhpa(s):
    for i in s:
        if not ('А' <= i <= 'Я' or 'а' <= i <= 'я'):
            return False
    return True


def lower(s):
    res = ''
    for i in s:
        if 'А' <= i <= 'Я':
            res += chr(ord(i) + ord('а') - ord('А'))
        else:
            res += i
    return res


def upper(s):
    res = ''
    for i in s:
        if 'а' <= i <= 'я':
            res += chr(ord(i) + ord('А') - ord('а'))
        else:
            res += i
    return res


def isupper(s):
    for i in s:
        if not ('А' <= i <= 'Я'):
            return False
    return True


def isexp(s):
    for i in s:
        if i not in digitOper:
            return False
    if any([i in '0123456789' for i in s]):
        return True
    return False


def calculate(s):
    res = 0
    if s[0] != '-':
        s = '+' + s
    if '.' in s:
        end = len(s) - 1
        for i in range(len(s) - 2, -1, -1):
            if s[i] in '+-':
                res += float(s[i:end + 1])
                end = i - 1
        return '{:.4f}'.format(res)
    else:
        end = len(s) - 1
        for i in range(len(s) - 2, -1, -1):
            if s[i] in '+-':
                res += int(s[i:end + 1])
                end = i - 1
        return str(res)


def replace(s, old, new):
    for i in range(len(s) - 1 - len(old) + 1, -1, -1):
        if s[i:i + len(old)] == old:
            s = s[:i] + new + s[i + len(old):]
    return s


def lfind(s, sub):
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            return i
    return -1
    

def split(s, sep):
    if s == '' or len(s) < len(s):
        return ['']
    else:
        res = []
        if s[0] != sep:
            s = sep + s
        if s[-1] != sep:
            s += sep
        begin = 0
        for i in range(1, len(s)):
            if s[i] == sep:
                res.append(s[begin + 1 : i])
                begin = i
        return res

    
def alignment(text, align):
    #Удаления двойных пробелов и пробелов в начале и конце строк    
    for i, line in enumerate(text):
        for j in range(len(line) - 2, -1, -1):
            if line[j:j+2] == '  ':
                line = line[:j + 1] + line[j + 2:]
        while line != '' and line[0] == ' ':
            line = line[1:]
        while line != '' and line[-1] == ' ':
            line = line[:-1]
        text[i] = line

    if align == 'width':
        #Поиск максимальной длины строки
        maxLen = 0
        for i, line in enumerate(text):
            if i == 0 or len(line) > maxLen:
                maxLen = len(line)
        # Формирование списка blacks с числом пробелов, которые должны 
        # ставиться после каждого слова в тексте
        blanks = []
        for i, line in enumerate(text):
            dBlanks = maxLen - len(line)
            plBlanks = len(split(line, ' ')) - 1
            if plBlanks == 0:
                blanks.append([0])
            else:
                blanks.append([dBlanks//plBlanks + 2] * (dBlanks - dBlanks // 
                plBlanks * plBlanks) + [dBlanks//plBlanks + 1] * (plBlanks - 
                dBlanks + dBlanks // plBlanks * plBlanks) + [0])
        #Разбиение строки на слова и сборка с необходимым числом пробелов
        for i, line in enumerate(text):
            words = split(line, ' ')
            resLine = ''
            for j, word in enumerate(words):
                resLine += word + ' '*(blanks[i][j])
            text[i] = resLine
    elif align == 'right':
        maxLen = 0
        for i, line in enumerate(text):
            if i == 0 or len(line) > maxLen:
                maxLen = len(line)
        for i, line in enumerate(text):
            text[i] = ' '*(maxLen - len(line)) + text[i]


def deleteWord(text):
    word = input("\nВведите слово для удаления: ")
    for i, line in enumerate(text):
        line = ' ' + line + ' '
        for j in range(len(line) - 2, 0, -1):
            if isalhpa(line[j]) and not isalhpa(line[j + 1]):
                end = j
            if isalhpa(line[j]) and not isalhpa(line[j - 1]):
                if lower(word) == lower(line[j:end + 1]):
                    line = line[:j] + line[end + 1:]

        #while '  ' in line:
        #    line = replace(line, '  ', ' ')
        #while line != '' and line[0] == ' ':
        #    line = line[1:]
        #while line != '' and line[-1] == ' ':
        #    line = line[:-1]
        if line[0] == ' ':
            line = line[1:]
        text[i] = line


def replaceWord(text):
    old = input("\nВведите слово, которое нужно заменить: ")
    new = input("Введите новое слово: ")
    for i, line in enumerate(text):
        line = ' ' + line + ' '
        for j in range(len(line) - 2, 0, -1):
            if isalhpa(line[j]) and not isalhpa(line[j + 1]):
                end = j
            if isalhpa(line[j]) and not isalhpa(line[j - 1]):
                if lower(old) == lower(line[j:end + 1]):
                    if isupper(line[j]):
                        line = (line[:j] + upper(new[0]) + new[1:] + 
                        line[end + 1:])
                    else:    
                        line = line[:j] + new + line[end + 1:]
        line = line[1:-1]
        text[i] = line


def arifmExp(text):
    for i, line in enumerate(text):
        line = ' ' + line + ' '
        for j in range(len(line) - 2, 0, -1):
            if line[j] in digitOper and line[j + 1] not in digitOper:
                end = j
            if line[j] in digitOper and line[j - 1] not in digitOper:
                exp = line[j:end + 1]
                if isexp(exp):
                    line = line[:j] + calculate(exp) + line[end + 1:]
        line = line[1:-1]
        text[i] = line


def formColumn(text):
    alignment(text, 'left')
    iMin = 0
    sNew = ''
    for i in range(len(text)):
        if i == 0 or len(text[iMin]) > len(text[i]):
            iMin = i
    words = split(text[iMin], ' ')
    lenMax = 0
    iLenMax = 0
    for i, word in enumerate(words):
        if len(word) > lenMax:
            lenMax = len(word)
            iLenMax = i
    for i in range(len(words[iLenMax])):
        for j in range(len(words)):
            #i - номер строки
            #j - номер слова
            if i < len(words[j]):
                sNew += words[j][i] + ' '
            else:
                sNew += '  '
        sNew += '\n'
    sNewArr = split(sNew, '\n')
    sNewArr = []
    begin = -1
    for i in range(1, len(sNew)):
        if sNew[i] == '\n':
            sNewArr.append(sNew[begin + 1 : i])
            begin = i
    return text[:iMin] + sNewArr + text[iMin + 1:]


def countWords(s):
    c = 0
    s += ' '
    for i in range(len(s) - 2):
        if isalhpa(s[i]) and not isalhpa(s[i+1]):
            c += 1
    return c


def sorting(text):
    textNew = ''
    for line in text:
        textNew += line + ' '
    text = []
    start = 0
    for i in range(len(textNew)):
        if textNew[i] == '.':
            text.append(textNew[start: i + 1])
            start = i + 1
    for i, line in enumerate(text):
        while line != '' and line[0] == ' ':
            line = line[1:]
        while line != '' and line[-1] == ' ':
            line = line[:-1]
        text[i] = line
    for i in range(len(text) - 1, 0, -1):
        for j in range(0, i):
            if countWords(text[j]) > countWords(text[j + 1]):
                line = text[j]
                text[j] = text[j + 1]
                text[j + 1] = line
    return text


def replaceWordWithout(TEXT):
    print(
    *[sent.replace(' '+min(sent.split(), key=len), " _", 1)
    .replace(' '+max(sent.split(), key=len), ' '+min(sent.split(), key=len), 1)
    .replace(" _", ' '+max(sent.split(), key=len),1)
    for sent in [' '.join(max([i.split() for i in TEXT.replace('\n', ' ')
    .split('.')], key=len))]], end='.\n'
    )


def writeLitters(text):
    maxCount = minCount = maxCountAll = minCountAll = 0
    for i, sens in enumerate(text):
        letCount = 0
        for let in sens:
            if lower(let) in sogLet:
                letCount += 1
        if i == 0 or letCount > maxCount:
            maxCount = letCount
            maxSens = sens
        if i == 0 or letCount < minCount:
            minCount = letCount
            minSens = sens
    print("\nПредложение с максимальным числом числом согласных букв ("
          +str(maxCount)+"):")
    print(maxSens)
    print("\nПредложение с минимальным числом числом согласных букв ("
          +str(minCount)+"):")
    print(minSens)


def main():
    text = split(TEXT, '\n')
    #align = 'left'
    #alignment(text, align)
    write(text)
    
    choice = None
    while choice != '0':
        text = split(TEXT, '\n')
        #align = 'left'
        #alignment(text, align)
        print(menu)
        choice = input("Ваш выбор: ")
        if choice == '1':
            align = 'width'
            alignment(text, align)
            write(text)
        elif choice == '2':
            align = 'left'
            alignment(text, align)
            write(text)
        elif choice == '3':
            align = 'right'
            alignment(text, align)
            write(text)
        elif choice == '4':
            replaceWord(text)
            #alignment(text, align)
            write(text)
        elif choice == '5':
            deleteWord(text)
            #alignment(text, align)
            write(text)
        elif choice == '6':
            arifmExp(text)
            #alignment(text, align)
            write(text)
        elif choice == '7':
            text = formColumn(text)
            write(text)
        elif choice == '10':
            text = sorting(text)
            write(text)
        elif choice == '9':
            replaceWordWithout(TEXT)
        elif choice == '8':
            writeLitters(sorting(text))
        elif choice == '0':
            print("\nВыход")
        else:
            print("\nДанного номера нет в меню")


main()
