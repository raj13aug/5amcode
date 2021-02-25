def add(x, y):
    return x+y


list1 = list(range(1, 5))
list2 = list(range(6, 10))
list3 = list(map(add, list1, list2))
print("Sum of", list1, "and", list2, "=", list3)
