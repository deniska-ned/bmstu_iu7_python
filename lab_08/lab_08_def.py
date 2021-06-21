from math import log10, floor

def f(x):
    return x*x

def F(x):
    return x*x*x/3

def numToStr(x, digit):
    if abs(x) >= 10**digit:
        return ('{:.'+str(digit)+'e}').format(x)
    if abs(x) >= 10**(digit-1):
        return str(int(x))
    if abs(x) < 0.1:
        return ('{:.'+str(digit-1)+'e}').format(x)
    if abs(x) < 1:
        return ('{:.'+str(digit)+'}').format(x)
    return str(round(x, 1-floor(log10(abs(x)))+digit))

def m_par(a, b, n):
    res = 0
    h = (b-a)/n
    for i in range(n//2):
        res += f(a+2*h*i)+4*f(a+h+2*h*i)+f(a+2*h+2*h*i)
    res *= h/3
    return res


print("f(x) = x^2")

a, b = map(float, input("\nВведите нижнюю и верхнюю границу ингрерования: "
).split())
while not b > a:
    print("Значение верхней границы должно быть больше, чем нижняя")
    a, b = map(float, input("\nВведите нижнюю и верхнюю границу ингрерования: "
).split())

n = int(input("Введите число разбиений: "))
while n <= 0 or n%2 != 0:
    if n%2 != 0:
        print("Число разбиений должно быть четно")
    if n <= 0:
        print("Число разбиений должно быть положительным")
    n = int(input("\nВведите число разбиений: "))

integ = m_par(a, b, n)

print("\nМетод парабол")
print("Значение определенного интеграла:", numToStr(integ, 7))

print("\nТочное значение через первообразную: ", numToStr(F(a)-F(b), 7))
