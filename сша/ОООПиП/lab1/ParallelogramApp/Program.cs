using ParallelogramApp;

class Program
{
    /// <summary>
    /// Главный метод программы.
    /// </summary>
    /// <param name="args">Аргументы командной строки.</param>
    static void Main(string[] args)
    {
        Console.WriteLine("Программа для работы с параллелограммом");

        var vertex1 = ReadPoint("Введите координаты вершины 1 (X, Y): ");
        var vertex2 = ReadPoint("Введите координаты вершины 2 (X, Y): ");
        var vertex3 = ReadPoint("Введите координаты вершины 3 (X, Y): ");
        var vertex4 = ReadPoint("Введите координаты вершины 4 (X, Y): ");

        Parallelogram parallelogram = new Parallelogram(vertex1, vertex2, vertex3, vertex4);

        if (!parallelogram.IsValid())
        {
            Console.WriteLine("Параллелограмм с данными координатами не существует.");
            return;
        }

        int choice;
        do
        {
            Console.WriteLine("\nВыберите действие:");
            Console.WriteLine("1. Вычислить периметр");
            Console.WriteLine("2. Вычислить площадь");
            Console.WriteLine("3. Проверить, принадлежит ли точка параллелограмму");
            Console.WriteLine("4. Выход");
            Console.Write("Ваш выбор: ");

            // Проверка на корректный ввод
            while (!int.TryParse(Console.ReadLine(), out choice) || choice < 1 || choice > 4)
            {
                Console.WriteLine("Некорректный ввод. Пожалуйста, выберите пункт от 1 до 4.");
            }

            switch (choice)
            {
                case 1:
                    Console.WriteLine($"Периметр параллелограмма: {parallelogram.GetPerimeter()}");
                    break;
                case 2:
                    Console.WriteLine($"Площадь параллелограмма: {parallelogram.GetArea()}");
                    break;
                case 3:
                    var point = ReadPoint("Введите координаты точки (X, Y): ");
                    if (parallelogram.IsPointInside(point.X, point.Y))
                    {
                        Console.WriteLine($"Точка ({point.X}, {point.Y}) принадлежит параллелограмму.");
                    }
                    else
                    {
                        Console.WriteLine($"Точка ({point.X}, {point.Y}) не принадлежит параллелограмму.");
                    }
                    break;
                case 4:
                    Console.WriteLine("Выход из программы.");
                    break;
            }

        } while (choice != 4); // Продолжать, пока пользователь не выберет выход
    }

    /// <summary>
    /// Читает координаты точки из ввода пользователя.
    /// </summary>
    /// <param name="prompt">Сообщение для запроса ввода.</param>
    /// <returns>Координаты точки как кортеж.</returns>
    static (double X, double Y) ReadPoint(string prompt)
    {
        Console.Write(prompt);
        var input = Console.ReadLine().Split(',');

        if (input.Length != 2 || !double.TryParse(input[0], out double x) || !double.TryParse(input[1], out double y))
        {
            Console.WriteLine("Неправильный ввод. Попробуйте снова.");
            return ReadPoint(prompt);
        }

        return (x, y);
    }
}