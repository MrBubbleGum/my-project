def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input("Введите натуральное число n: "))

if n < 1:
    print("Пожалуйста, введите натуральное число больше 0.")
else:

    result = factorial(n)
    print(f"Факториал числа {n} равен {result}")