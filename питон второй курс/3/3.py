def create_html_list(strings):
    def inner_function(): 
        # Внутренняя функция использует переменную из внешней функции
        result = "<ol>\n"
        for string in strings:
            result += f"<li>{string}</li>\n"
        result += "</ol>"
        return result
    
    return inner_function()


num_strings = int(input("Введите количество строк: "))
if num_strings <= 0:
    print("Введите число больше нуля")
else:
    user_strings = []
    for i in range(num_strings):
        user_strings.append(input(f"Введите строку {i+1}: "))
    
    # Вызов главной функции с переданными строками
    html_list = create_html_list(user_strings)
    print(html_list)
