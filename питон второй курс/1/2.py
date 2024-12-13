a = int(input("введите время в минутах: "))
b = int(input("Введите время в секундах ")) 

if (a>=0 and b>=0):
    result = f"{a} минут(ы) - больше" if (a * 60) > b else f"{b} секунд - больше" if (a * 60) < b else "Равны"
    print(result)
else:
    print ("Проверьте данные")
    



