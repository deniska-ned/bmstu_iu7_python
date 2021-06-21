import random

def generage_sorted_array(size):
    return [i for i in range(size)]

def generage_reverse_sorted_array(size):
    return [i for i in range(size - 1, 0 - 1, -1)]

def generage_random_array(size):
    return [random.randint(-size, size) for i in range(size)]

if __name__ == "__main__":
    print("This is package file")
