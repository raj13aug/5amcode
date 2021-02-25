name = 'raja'
age = 35

print("Name is", name, "My age is", age)
print("Name is %s,marks are %i" % (name, age))

print("Name is {1}, Marks are {0}".format(name, age))

lst = [int(x) for x in input("enter the number by comma").split(',')]
print(lst)
