def sum(num1, num2):
    res = [0] * 9
    add = 0
    for i in range(7, -1, -1):
        if num1[i] + num2[i] + add == 3:
            res[i+1] = 1
            add = 1
        elif num1[i] + num2[i] + add == 2:
            res[i+1] = 0
            add = 1
        elif num1[i] + num2[i] + add == 1:
            res[i+1] = 1
            add = 0
        else:
            res[i+1] = 0
            add = 0
    return res[1:]


def decToBin(n, bits = 8):
    mask = (1 << bits) - 1
    if n < 0:
        n = (abs(n) ^ mask) + 1   
    n = n & mask

    binNum = [0] * 8
    for i in range(8):
        binNum[8 - i - 1] = n % 2
        n //= 2

    return binNum


def binToDec(num, bits = 8):
    mask = (1 << bits) - 1

    decNum = 0
    for i in range(0, 8, 1):
        decNum += num[8 - i - 1] * 2**i

    if num[0] == 1:
        decNum = -((decNum - 1) ^ mask)
    return decNum


if __name__ == "__main__":
    print("This is package file")