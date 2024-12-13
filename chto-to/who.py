def kod(arr, tg):
    left, right = 0, len(arr) - 1

    while left <= right:
        m1 = left + (right - left) // 3
        m2 = right - (right - left) // 3

        if arr[m1] == tg:
            return m1
        elif arr[m2] == tg:
            return m2
        elif tg < arr[m1]:
            right = m1 - 1
        elif tg > arr[m2]:
            left = m2 + 1
        else:
            left = m1 + 1
            right = m2 - 1

    return -1

def arry():
    arr = []
    l = int(input("размер массива: "))
    for _ in range(l):
        n = int(input("элемент массива: "))
        arr.append(n)
    return arr

def sch():
    arr = arry()
    tg = int(input("нужное число: "))
    result = kod(arr, tg)

    if result != -1:
        print(f"элемент в позиции {result + 1}")  # Выводим позицию на единицу больше
    else:
        print("элемент не найден")

def main():
    sch()

if __name__ == "__main__":
    main() 