
n = int(input("Введите сумму n: "))
while n <= 0:
    print("Сумма должна быть больше нуля. Попробуйте снова.")
    n = int(input("Введите сумму n (больше 0): "))

bills = [64, 32, 16, 8, 4, 2, 1]

used_bills = []

for bill in bills:
    while n >= bill:  
        used_bills.append(bill)  
        n -= bill  
print("Купюры для формирования суммы:", used_bills)

