
word = input("Введите слово: ")

if not word:
    print ("Слово не было введено")
else:

    if word == "RECT":
        def get_sq(length, width):
        
            return length * width
    else:
        def get_sq(length, width):
    
            return 2 * (length + width)

    length = float(input("Введите длину: "))
    width = float(input("Введите ширину: "))

    result = get_sq(length, width)
    print("Результат:", result)