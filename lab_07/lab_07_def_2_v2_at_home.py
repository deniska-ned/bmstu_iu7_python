from math import ceil

#Ввод M, N, Z
M = int(input("Введите число строк матрицы: "))
while not 1 <= M <= 6:
    print("Допустимое число строк от 1 до 6")
    M = int(input("\nВведите число строк матрицы: "))
    
N = int(input("Введите число столбцов матрицы: "))
while (not 1 <= N <= 8) or (N*M < 2):
    if (N*M < 2):
        print("В матрице дожно быть не меньше 2 элементов")
    else:
        print("Допустимое число стрлбцов от 1 до 8")
    N = int(input("\nВведите число столбцов матрицы: "))

Z=[]
print()
for i in range(M):
    Zi = list(map(int, input("Введите в строку значеия строки №{:d}: ".format(
i+1)).split()))
    while len(Zi) != N:
        print("В строке должно быть элементов",N)
        Zi = list(map(int, input("\nВведите в строку значеия строки №{:d}: "
.format(i+1)).split()))
    Z.append(Zi)

#Вывод введенной матрицы Z
print("\nВведенная матрица:")
#Вывод строки с номерами столбцов
for i in range(N+1):
    if i == 0:
        print('\\'+' '*7, end='')
    else:
        print(i, '.\t', sep='',end='')
print()
#Вывод значений
for i in range(M):
    print(i+1, '.\t', sep='',end='')
    for j in range(N):
        print(Z[i][j], '\t', sep='',end='')
    print()

#Ввод l
l = int(input("\nВведите число элементов в строке для вывода: "))
while not 2 <= l <= min([5, N]):
    print("Допустимое значение от 2 до", min([5, N]))
    l = int(input("\nВведите число элементов в строке для вывода: "))

#Вывод
for num_blocks in range(ceil(N/l)):
    #Вывод элементов
    if num_blocks == ceil(N/l) - 1:
        k = N%l
    else:
        k = l
    #Вывод строки с номера столбцов
    print('\\'+' '*7, end='')
    for i in range(k):
        print(l*num_blocks+i+1, '.\t', sep='', end='')
    print()
    for i in range(M):
        print(i+1, '.\t', sep='', end='')
        for j in range(k):
            print(Z[i][num_blocks*l + j], end='\t')
        print()
    print()
