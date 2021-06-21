try:
    g1 = open('g1.txt', 'r')
    g2 = open('g2.txt', 'w')
    g2.close()
except FileNotFoundError:
    print('Файл не найден')
except Exception as ex:
    print('Неизвестная ошибка:', ex)
else:
    for i in g1:
        if i == '' or i[len(i)-1] != '\n':
            i += '\n'
        
        g2 = open('g2.txt', 'r')
        repeat = False
        for j in g2:
            if j == '' or j[len(j)-1] != '\n':
                j += '\n'
            if i == j:
                repeat = True
        g2.close()
        if not repeat:
            g2 = open('g2.txt', 'a')
            g2.write(i)
            g2.close
    print('Перезапись выполнена')
    g1.close()