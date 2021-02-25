dict1 = {'Name': 'Nataraj', 'colour': 'black'}

print(dict1.items())

k = dict1.keys()
courses = {'raja': ["math", "scenice", "social"],
           'pradheep': ["tamil", "programming"]}
keys = courses.keys()
for name in keys:
    print("The course taken by", name)
    for listofcourse in courses[name]:
        print(listofcourse)
