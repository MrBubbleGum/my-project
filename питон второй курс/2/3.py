while True:
    cities_input = input("Введите названия городов через пробел: ")
    long_cities = [city for city in cities_input.split() if len(city) > 5]
    if long_cities:
        print("Города с длиной более 5 символов:", long_cities)
        break  
    else:
        print("Пожалуйста, введите хотя бы один город с длиной более 5 символов.")