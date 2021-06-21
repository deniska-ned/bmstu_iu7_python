#лб7, защита 2


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

print("\nВведенная матрица:")
#Вывод строки с номерами столбцов
for i in range(N+1):
    if i == 0:
        print('\\'+" "*7, end='')
    else:
        print(i, end="\t")
print()
#Вывод матрицы
for i in range(M):
    print(i+1, end="\t")
    for j in range(N):
        print(Z[i][j], end="\t")
    print()


l = int(input("\nВведите число элементов в строке для вывода: "))
while not 2 <= l <= min([5, N]):
    print("Допустимое значение от 2 до", min([5, N]))
    l = int(input("\nВведите число элементов в строке для вывода: "))

print("\nВывод: ")
#Вывод строки с номерами столбцов
print(end="\\"+" "*7)
for i in range(l):
    print(i+1, end='\t')
print()

#Вывод матрицы
row_num = 1
print(row_num, end='\t')
row_num += 1

i = 0
j = 0
while i*N + j + 1 <= M*N:
    print(Z[i][j], end='\t')
    if (i*N + j + 1)%l == 0 and i*N+j +1 != M*N:
        print("\n", row_num, '\t', sep='',end='')
        row_num += 1
    if j == N-1:
        j = 0
        i += 1
    else:
        j += 1
