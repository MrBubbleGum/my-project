guests = set()

while True:
    name = input("Введите имя гостя (или нажмите Enter для завершения): ")
    if name == "":
        break
    guests.add(name.strip().lower()) 

print("Общее число гостей:", len(guests))