from main import *

allTest = True

print("EightBitAdder.decToBin\n")

testData = (
    (1,     [0, 0, 0, 0, 0, 0, 0, 1]),
    (5,     [0, 0, 0, 0, 0, 1, 0, 1]),
    (-128,  [1, 0, 0, 0, 0, 0, 0, 0]),
    (-1,    [1, 1, 1, 1, 1, 1, 1, 1]),
    (-10,   [1, 1, 1, 1, 0, 1, 1, 0]),
)

for input, exceptOutput in testData:
    output = EightBitAdder.decToBin(input)
    
    iTest = output == exceptOutput
    allTest = allTest and iTest
    
    print("input        =", input)
    print("output       =", output)
    print("exceptOutput =", exceptOutput)
    print("Res          =", iTest, end='\n' * 2)

print(allTest)
print('=' * 50)

# =========================================== #

allTest = True

print("EightBitAdder.binToDec\n")

testData = (
    ([0, 0, 0, 0, 0, 0, 0, 0], 0),
    ([0, 0, 0, 0, 0, 0, 0, 1], 1),
    ([0, 0, 0, 0, 0, 1, 0, 1], 5),
    ([0, 0, 0, 0, 0, 1, 1, 1], 7),
    ([1, 0, 0, 0, 0, 0, 0, 0], -128),
    ([1, 1, 1, 1, 1, 1, 1, 1], -1),
    ([1, 1, 1, 1, 0, 1, 1, 0], -10),
)

for input, exceptOutput in testData:
    output = EightBitAdder.binToDec(input)
    
    iTest = output == exceptOutput
    allTest = allTest and iTest
    
    print("input        =", input)
    print("output       =", output)
    print("exceptOutput =", exceptOutput)
    print("Res          =", iTest, end='\n' * 2)

print(allTest)
print('=' * 50)

# =========================================== #