from functools import reduce


def add(x, y):
    return x+y


list1 = list(range(1, 5))

result = reduce(add, list1)
print(result)
