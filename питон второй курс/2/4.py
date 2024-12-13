
input_lines = []

while True:
    line = input("Введите строки с целыми числами (или нажмите Enter для завершения): ")
    if line == "":
        break
    input_lines.append(line)

two_dimensional_list = [list(map(int, line.split())) for line in input_lines]

print(two_dimensional_list)