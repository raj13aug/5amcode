x = int(input("Enter the Min number "))
y = int(input("Enter the Max number "))

i = x

if i % 2 == 0:
    i += 1
while i <= y:
    print(i)
    i += 2
