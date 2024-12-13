import os
from tkinter import filedialog, Tk

# Определяем заголовки для текстового файла
FIELDS = ['УДК кассеты', 'Название фильма', 'Жанр', 'Производитель', 'Год выпуска', 'Дата проката', 'Время проката']
FIELD_SEPARATOR = ','  # Разделитель для CSV файла

# Функция для инициализации базы данных
def initialize_database(filename):
    """Инициализирует файл базы данных, если он не существует."""
    if not os.path.exists(filename):
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(FIELD_SEPARATOR.join(FIELDS) + '\n')  # Запись заголовков в файл

# Функция для добавления записи в базу данных
def add_record(filename, record):
    """Добавляет запись в файл базы данных."""
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(FIELD_SEPARATOR.join(record) + '\n')

# Функция для удаления записи по индексу
def delete_record(filename, index):
    """Удаляет запись по индексу."""
    rows = []
    with open(filename, mode='r', encoding='utf-8') as file:
        rows = file.readlines()

    if index > 0 and index < len(rows):  # Исправляем проверку индекса
        rows.pop(index)
    
    with open(filename, mode='w', encoding='utf-8') as file:
        file.writelines(rows)

# Функция для вывода записи в табличном виде
def print_table(header, rows):
    """Выводит данные в виде таблицы."""
    print(f"{' | '.join(header)}")
    print("-" * 100)  # Разделительная линия
    for row in rows:
        print(f"{' | '.join(row)}")

# Функция для поиска по одному полю с табличным выводом
def search_by_field(filename, field, value):
    """Поиск по одному полю и вывод всех соответствующих строк в табличном виде с фиксированной шириной колонок."""
    # Заданные размеры для колонок
    column_widths = [5, 20, 15, 20, 10, 10, 10]
    results = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            rows = file.readlines()
            header = rows[0].strip().split(FIELD_SEPARATOR)
            
            # Проверка на корректность индекса поля
            if field >= len(header):
                print(f"Ошибка: индекс поля {field} превышает количество колонок.")
                return []

            for row in rows[1:]:
                columns = row.strip().split(FIELD_SEPARATOR)
                # Проверка наличия значения в нужном поле
                if len(columns) > field and value.lower() in columns[field].lower():
                    results.append(columns)
            
            # Функция для вывода строки с выравниванием по колонкам
            def format_row(row):
                return ''.join([str(value).ljust(width) for value, width in zip(row, column_widths)])

            # Выводим результаты в табличном виде
            if results:
                # Выводим заголовок
                print(format_row(header))
                print('-' * sum(column_widths))  # Разделительная линия

                # Выводим результаты
                for record in results:
                    print(format_row(record))
            else:
                print(f"Нет результатов для поиска по полю '{header[field]}' с значением '{value}'.")

    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    
    return results



# Функция для поиска по двум полям с табличным выводом
def search_by_two_fields(filename, field1, value1, field2, value2):
    """Поиск по двум полям и вывод результатов в табличном виде с фиксированной шириной колонок."""
    # Заданные размеры для колонок
    column_widths = [5, 20, 15, 20, 10, 10, 10]
    results = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            rows = file.readlines()
            header = rows[0].strip().split(FIELD_SEPARATOR)
            
            # Проверка на корректность индексов полей
            if field1 >= len(header) or field2 >= len(header):
                print("Ошибка: один из индексов полей превышает количество колонок.")
                return []

            for row in rows[1:]:
                columns = row.strip().split(FIELD_SEPARATOR)
                # Проверка наличия значения в нужных полях
                if len(columns) > field1 and len(columns) > field2:
                    if value1.lower() in columns[field1].lower() and value2.lower() in columns[field2].lower():
                        results.append(columns)
            
            # Функция для вывода строки с выравниванием по колонкам
            def format_row(row):
                return ''.join([str(value).ljust(width) for value, width in zip(row, column_widths)])

            # Выводим результаты в табличном виде
            if results:
                # Выводим заголовок
                print(format_row(header))
                print('-' * sum(column_widths))  # Разделительная линия

                # Выводим результаты
                for record in results:
                    print(format_row(record))
            else:
                print(f"Нет результатов для поиска по полям '{header[field1]}' и '{header[field2]}' с значениями '{value1}' и '{value2}'.")

    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    
    return results


# Функция для замены УДК кассеты для заданного фильма
def replace_udc(filename, movie_name, new_udc):
    """Заменяет УДК кассеты для заданного фильма."""
    rows = []
    with open(filename, mode='r', encoding='utf-8') as file:
        rows = file.readlines()

    for i in range(1, len(rows)):  # Пропускаем заголовок
        columns = rows[i].strip().split(FIELD_SEPARATOR)
        if columns[1].lower() == movie_name.lower():  # Фильтр по названию фильма
            columns[0] = new_udc
            rows[i] = FIELD_SEPARATOR.join(columns) + '\n'
    
    with open(filename, mode='w', encoding='utf-8') as file:
        file.writelines(rows)

# Функция для удаления записей по году выпуска
def delete_by_year(filename, year):
    """Удаляет все записи о фильмах с заданным годом выпуска."""
    rows = []
    with open(filename, mode='r', encoding='utf-8') as file:
        rows = file.readlines()

    rows_to_keep = [rows[0]]  # Сохраняем заголовок
    for row in rows[1:]:
        columns = row.strip().split(FIELD_SEPARATOR)
        if columns[4] != str(year):
            rows_to_keep.append(row)

    with open(filename, mode='w', encoding='utf-8') as file:
        file.writelines(rows_to_keep)

def display_records(filename):
    """Выводит все записи из базы данных в виде таблицы с фиксированной шириной колонок."""
    # Заданные размеры для колонок
    column_widths = [5, 20, 15, 20, 10, 10, 10]

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            rows = file.readlines()
            header = rows[0].strip().split(FIELD_SEPARATOR)
            results = []
            for row in rows[1:]:  # Пропускаем заголовок
                columns = row.strip().split(FIELD_SEPARATOR)
                results.append(columns)
            
            # Функция для вывода строки с выравниванием по колонкам
            def format_row(row):
                return ''.join([str(value).ljust(width) for value, width in zip(row, column_widths)])

            # Выводим заголовок
            print(format_row(header))
            print('-' * sum(column_widths))  # Разделительная линия

            # Выводим данные
            for record in results:
                print(format_row(record))

    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


# Функция для выбора файла через диалоговое окно
def select_file():
    """Позволяет пользователю выбрать файл для работы."""
    root = Tk()
    root.withdraw()  # Скрыть главное окно
    filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not filename:
        raise ValueError("Файл не выбран.")
    return filename

# Основная программа
def main():
    try:
        # Выбор файла для работы
        filename = select_file()
        
        # Инициализация базы данных
        initialize_database(filename)
        
        while True:
            # Меню программы
            print("\nМеню:")
            print("1. Добавить запись")
            print("2. Удалить запись")
            print("3. Показать все записи")
            print("4. Поиск по одному полю")
            print("5. Поиск по двум полям")
            print("6. Заменить УДК кассеты фильма")
            print("7. Удалить фильмы по году выпуска")
            print("8. Выход")
            
            choice = input("Выберите опцию: ")

            if choice == "1":
                # Добавление записи
                record = []
                for field in FIELDS:
                    value = input(f"Введите {field}: ")
                    record.append(value)
                add_record(filename, record)

            elif choice == "2":
                # Удаление записи
                index = int(input("Введите индекс записи для удаления: "))
                delete_record(filename, index)

            elif choice == "3":
                # Показать все записи
                display_records(filename)

            elif choice == "4":
                # Поиск по одному полю
                while True:
                    field = int(input(f"Выберите поле для поиска (0 - {len(FIELDS)-1}): "))
                    value = input("Введите значение для поиска: ")
                    results = search_by_field(filename, field, value)
                    
                    # Если результатов нет, предложить повторить поиск
                    if not results:
                        repeat = input("Результаты не найдены. Хотите попробовать снова? (y/n): ").lower()
                        if repeat != 'y':
                            break
                    else:
                        break  # Прекращаем поиск, если результаты найдены

            elif choice == "5":
                # Поиск по двум полям
                field1 = int(input(f"Выберите первое поле для поиска (0 - {len(FIELDS)-1}): "))
                value1 = input("Введите значение для первого поля: ")
                field2 = int(input(f"Выберите второе поле для поиска (0 - {len(FIELDS)-1}): "))
                value2 = input("Введите значение для второго поля: ")
                results = search_by_two_fields(filename, field1, value1, field2, value2)

            elif choice == "6":
                # Заменить УДК кассеты
                movie_name = input("Введите название фильма: ")
                new_udc = input("Введите новый УДК кассеты: ")
                replace_udc(filename, movie_name, new_udc)

            elif choice == "7":
                # Удалить по году выпуска
                year = int(input("Введите год выпуска для удаления: "))
                delete_by_year(filename, year)

            elif choice == "8":
                # Выход
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
