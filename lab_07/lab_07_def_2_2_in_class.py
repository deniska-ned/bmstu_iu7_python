from math import ceil

#Ввод М, N
M = int(input("Введите число строк матрицы: "))
while not 1 <= M <= 6:
    print("Допустимое число строк от 1 до 6")
    M = int(input("\nВведите число строк матрицы: "))

N = int(input("Введите число столбцов матрицы: "))
while not 2 <= N <= 8:
    print("Допустимое число столбцов от 2 до 8")
    N = int(input("\nВведите число столбцов матрицы: "))
    
Z = []

#Ввод матрицы
print("\nВвод матрицы: ")
for i in range(M):
    Zi = list(map(int, input("Введите строку №{:d}: ".format(i+1)).split()))
    while len(Zi) != N:
        print("В строке должно быть количество символов", N)
        Zi = list(map(int, input("\nВведите строку №{:d}: ".format(i+1)).split(
)))
    Z.append(Zi)

#Вывод матрицы
print("\nВведенная матрица: ")
#Вывод строки с номерами столбоцов
print('\t', end='')
for i in range(N):
    print(i+1, end='\t')
print()
#Вывод значений
for i in range(M):
    print(i+1, end='\t')
    for j in range(N):
        print(Z[i][j], end='\t')
    print()
        
#Ввод l
l = int(input("\nВведите число столбцов для вывода матрицы: "))
while not 2 <= l <= min(N, 5):
    print("Допустимое число столбцов для вывода от {:d} до {:d}".format(2,
min(N, 5)))
    l = int(input("\nВведите число столбцов для вывода матрицы: "))

#Вывод матрицы по l элементов в столбце
print("\nРезультат:")
for block_num in range(ceil(N/l)):
    if block_num == ceil(N/l) - 1:
        k = N - l*block_num
    else:
        k = l
    #Вывод строки с номерами столбоцов
    print('\t', end='')
    for i in range(k):
        print(l*block_num+i+1, end='\t')
    print()
    
    #Вывод значений
    for i in range(M):
        print(i+1, end='\t')
        for j in range(k):
            print(Z[i][l*block_num+j], end='\t')
        print()
    print()
