def check(x):
    if (x % 2 == 0 or x % 4 == 0):
        return x


evens = list(filter(check, range(2, 22)))
print(evens)


x = list(range(2, 23))
result = list(filter(lambda x: x % 2 == 0 or x % 4 == 0, x))
print(result)
