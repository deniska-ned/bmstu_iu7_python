s = input('Введите строку: ')
s = ' ' + s + ' '
for i in range(1, len(s) - 1):
    if s[i] == ' ' and s[i+1] != ' ':
        i_s = i+1
    if s[i] in ['X','Y','Z'] and s[i+1] != ' ':
        s = s[:i+1] + 'W' + s[i+2:]
    if s[i] == 'A' and s[i+1] == ' ' and s[i-1] != ' ':
        s = s[:i_s] + 'D' + s[i_s+1:]

s = s[1:len(s)-1]
print('Результат:',s)
