#Защита ЛБ

LEN = 8

'''
LEN = int(input("Введите длину квадратной матрицы: "))
while LEN < 2:
    print("Длина матрицы должна быть больше 1")
    LEN = int(input("\nВведите длину квадратной матрицы: "))
'''

K = int(input("Введите номер строки: "))
while not 1 <= K <= LEN:
    print("Значение номера строки должно быть от 1 до",LEN)
    K = int(input("\nВведите номер строки: "))

L = int(input("Введите номер столбца: "))
while not 1 <= L <= LEN:
    print("Значение номера столбца должно быть от 1 до",LEN)
    L = int(input("\nВведите номер строки: "))

A = [['.' for i in range(LEN)] for i in range(LEN)]

for i in range(LEN):
    A[K-1][i]='*'
    A[i][L-1]='*'
    if 0 <= ((K-L) + i) < LEN:
        A[(K-L) + i][i]='*'
    if 0 <= ((K-1+L-1)-i) < LEN:
        A[(K-1+L-1)-i][i]='*'

A[K-1][L-1]='F'

print('\n   ', end='')
for i in range(LEN):
    print('{:<3d}'.format(i+1), end='')
print('\n')
for i in range(LEN):
    print('{:<3d}'.format(i+1), end='')
    for j in range(LEN):
        print('{:<3}'.format(A[i][j]),end='')
    print()
