
students = input("Имена: ").split()
i = 0
while i < len(students):
    name = students[i]

    if name[0].lower() == name[-1].lower():
        print("Есть")
        break
    i += 1
else:
    print("Нет")