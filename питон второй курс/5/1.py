import math

class Segment:
    def __init__(self, x1=0, y1=0, x2=1, y2=1):
        # Проверка на корректность координат
        if not all(isinstance(i, (int, float)) for i in [x1, y1, x2, y2]):
            print("Некорректные данные. Создается отрезок с координатами (0,0) и (1,1).")
            self.__x1, self.__y1, self.__x2, self.__y2 = 0, 0, 1, 1
        else:
            self.__x1, self.__y1, self.__x2, self.__y2 = x1, y1, x2, y2
    
    # Свойства для доступа к координатам
    @property
    def x1(self):
        return self.__x1
    
    @property
    def y1(self):
        return self.__y1
    
    @property
    def x2(self):
        return self.__x2
    
    @property
    def y2(self):
        return self.__y2
    
    # Свойство для вычисления длины отрезка
    @property
    def length(self):
        return math.sqrt((self.__x2 - self.__x1)**2 + (self.__y2 - self.__y1)**2)
    
    # Метод для проверки, лежит ли отрезок на одной из осей координат
    def is_on_axis(self):
        return (self.__y1 == 0 and self.__y2 == 0) or (self.__x1 == 0 and self.__x2 == 0)

    # Метод для перемещения отрезка по вертикали
    def move_vertical(self, delta_y):
        self.__y1 += delta_y
        self.__y2 += delta_y

    # Метод для увеличения длины отрезка
    def increase_length(self, delta_length):
        current_length = self.length
        if current_length > 0:
            scale_factor = (current_length + delta_length) / current_length
            self.__x2 = self.__x1 + (self.__x2 - self.__x1) * scale_factor
            self.__y2 = self.__y1 + (self.__y2 - self.__y1) * scale_factor

    # Статический метод для проверки пересечения двух отрезков
    @staticmethod
    def are_intersecting(segment1, segment2):
        def ccw(A, B, C):
            return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

        def is_between(a, b, c):
            return min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= c[1] <= max(a[1], b[1])

        def on_segment(A, B, C):
            # Проверка, лежит ли точка C на отрезке AB
            return is_between(A, B, C)

        A = (segment1.x1, segment1.y1)
        B = (segment1.x2, segment1.y2)
        C = (segment2.x1, segment2.y1)
        D = (segment2.x2, segment2.y2)

        # Проверка на общие пересечения отрезков
        if ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D):
            return True

        # Дополнительная проверка для случаев касания или пересечения на границах
        if on_segment(A, B, C) or on_segment(A, B, D) or on_segment(C, D, A) or on_segment(C, D, B):
            return True

        return False

    # Строковое представление объекта
    def __str__(self):
        return f"({self.__x1};{self.__y1}), ({self.__x2};{self.__y2})"
    
# Программа для создания и манипулирования отрезками
def main():
    segments = []
    
    # Первый отрезок всегда создается с координатами (0, 0) и (1, 1)
    segment1 = Segment(0, 0, 1, 1)
    segments.append(segment1)

    # Считываем данные для второго и третьего отрезков
    for i in range(2, 4):
        print(f"Введите координаты для отрезка {i}:")
        try:
            x1 = float(input("Введите x1: "))
            y1 = float(input("Введите y1: "))
            x2 = float(input("Введите x2: "))
            y2 = float(input("Введите y2: "))
        except ValueError:
            print("Некорректные данные. Создается отрезок с координатами (0,0) и (1,1).")
            x1, y1, x2, y2 = 0, 0, 1, 1
        
        segment = Segment(x1, y1, x2, y2)
        segments.append(segment)
    
    # Функция для отображения информации об отрезках
    def print_segments_info():
        print(f"\n{'№':<5} {'Координаты границ':<30} {'Длина':<10} {'Лежит ли на оси координат'}")
        for i, seg in enumerate(segments, start=1):
            axis_status = "да" if seg.is_on_axis() else "нет"
            print(f"{i:<5} {str(seg):<30} {seg.length:<10.4f} {axis_status}")

    # Изначальная информация об отрезках
    print_segments_info()

    # Проверяем, пересекаются ли отрезки
    if Segment.are_intersecting(segments[0], segments[1]):
        print("\nОтрезки 1 и 2 пересекаются.")
    else:
        print("\nОтрезки 1 и 2 не пересекаются.")

    if Segment.are_intersecting(segments[0], segments[2]):
        print("Отрезки 1 и 3 пересекаются.")
    else:
        print("Отрезки 1 и 3 не пересекаются.")
    
    # Спрашиваем, с каким отрезком пользователь хочет работать
    segment_choice = int(input("\nВыберите номер отрезка для изменения (2 или 3): "))
    if segment_choice not in [2, 3]:
        print("Неверный выбор отрезка!")
        return

    # Предлагаем действия с выбранным отрезком
    action = input(f"\nВы выбрали отрезок {segment_choice}. Выберите действие (1 - переместить, 2 - увеличить длину): ")
    if action == "1":
        delta_y = float(input("Введите величину перемещения по вертикали: "))
        segments[segment_choice - 1].move_vertical(delta_y)
        print(f"\nНовый отрезок {segment_choice}: {segments[segment_choice - 1]}")
    elif action == "2":
        delta_length = float(input("Введите величину увеличения длины: "))
        segments[segment_choice - 1].increase_length(delta_length)
        print(f"\nНовый отрезок {segment_choice}: {segments[segment_choice - 1]}")
    else:
        print("Неверный выбор действия.")

    # Повторно выводим информацию после изменений
    print("\nПосле изменений:")
    print_segments_info()

    # Проверяем пересечение отрезков после изменений
    if Segment.are_intersecting(segments[0], segments[1]):
        print("\nОтрезки 1 и 2 пересекаются.")
    else:
        print("\nОтрезки 1 и 2 не пересекаются.")

    if Segment.are_intersecting(segments[0], segments[2]):
        print("Отрезки 1 и 3 пересекаются.")
    else:
        print("Отрезки 1 и 3 не пересекаются.")

if __name__ == "__main__":
    main()
0