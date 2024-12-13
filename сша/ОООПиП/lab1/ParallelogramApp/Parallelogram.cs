using System;

namespace ParallelogramApp
{
    /// <summary>
    /// Класс, представляющий параллелограмм на плоскости.
    /// </summary>
    public class Parallelogram
    {
        /// <summary>
        /// Получает или задает координаты первой вершины параллелограмма.
        /// </summary>
        public (double X, double Y) Vertex1 { get; set; }

        /// <summary>
        /// Получает или задает координаты второй вершины параллелограмма.
        /// </summary>
        public (double X, double Y) Vertex2 { get; set; }

        /// <summary>
        /// Получает или задает координаты третьей вершины параллелограмма.
        /// </summary>
        public (double X, double Y) Vertex3 { get; set; }

        /// <summary>
        /// Получает или задает координаты четвертой вершины параллелограмма.
        /// </summary>
        public (double X, double Y) Vertex4 { get; set; }

        /// <summary>
        /// Инициализирует новый экземпляр класса <see cref="Parallelogram"/>.
        /// </summary>
        /// <param name="vertex1">Координаты первой вершины.</param>
        /// <param name="vertex2">Координаты второй вершины.</param>
        /// <param name="vertex3">Координаты третьей вершины.</param>
        /// <param name="vertex4">Координаты четвертой вершины.</param>
        public Parallelogram((double X, double Y) vertex1, (double X, double Y) vertex2, (double X, double Y) vertex3, (double X, double Y) vertex4)
        {
            Vertex1 = vertex1;
            Vertex2 = vertex2;
            Vertex3 = vertex3;
            Vertex4 = vertex4;
        }

        /// <summary>
        /// Проверяет, является ли параллелограмм допустимым.
        /// </summary>
        /// <returns>True, если параллелограмм допустим; иначе false.</returns>
        public bool IsValid()
        {
            return AreParallel(Vertex1, Vertex2, Vertex3, Vertex4) && AreParallel(Vertex2, Vertex3, Vertex4, Vertex1);
        }

        /// <summary>
        /// Проверяет, являются ли две пары отрезков параллельными.
        /// </summary>
        /// <param name="v1">Первая вершина первой пары.</param>
        /// <param name="v2">Вторая вершина первой пары.</param>
        /// <param name="v3">Первая вершина второй пары.</param>
        /// <param name="v4">Вторая вершина второй пары.</param>
        /// <returns>True, если отрезки параллельны; иначе false.</returns>
        private bool AreParallel((double X, double Y) v1, (double X, double Y) v2, (double X, double Y) v3, (double X, double Y) v4)
        {
            double dx1 = v2.X - v1.X; // Изменение по X для первого отрезка
            double dy1 = v2.Y - v1.Y;
            double dx2 = v4.X - v3.X; // Изменение по X для второго отрезка
            double dy2 = v4.Y - v3.Y;

            return (dx1 * dy2) == (dx2 * dy1);
        }

        /// <summary>
        /// Вычисляет длину отрезка между двумя вершинами.
        /// </summary>
        /// <param name="v1">Первая вершина.</param>
        /// <param name="v2">Вторая вершина.</param>
        /// <returns>Длину отрезка как <see cref="double"/>.</returns>
        private double SideLength((double X, double Y) v1, (double X, double Y) v2)
        {
            return Math.Sqrt(Math.Pow(v2.X - v1.X, 2) + Math.Pow(v2.Y - v1.Y, 2));
        }

        /// <summary>
        /// Получает периметр параллелограмма.
        /// </summary>
        /// <returns>Периметр параллелограмма как <see cref="double"/>.</returns>
        public double GetPerimeter()
        {
            return 2 * (SideLength(Vertex1, Vertex2) + SideLength(Vertex2, Vertex3));
        }

        /// <summary>
        /// Получает площадь параллелограмма.
        /// </summary>
        /// <returns>Площадь параллелограмма как <see cref="double"/>.</returns>
        public double GetArea()
        {
            double baseLength = SideLength(Vertex1, Vertex2);
            double height = Math.Abs(Vertex3.Y - Vertex1.Y);
            return baseLength * height;
        }

        /// <summary>
        /// Проверяет, находится ли данная точка внутри параллелограмма.
        /// </summary>
        /// <param name="x">Координата X точки.</param>
        /// <param name="y">Координата Y точки.</param>
        /// <returns>True, если точка внутри параллелограмма; иначе false.</returns>
        public bool IsPointInside(double x, double y)
        {
            double areaOriginal = GetArea();
            double area1 = CalculateTriangleArea(Vertex1, Vertex2, (x, y));
            double area2 = CalculateTriangleArea(Vertex2, Vertex3, (x, y));
            double area3 = CalculateTriangleArea(Vertex3, Vertex4, (x, y));
            double area4 = CalculateTriangleArea(Vertex4, Vertex1, (x, y));

            return Math.Abs(areaOriginal - (area1 + area2 + area3 + area4)) < 0.0001;
        }

        /// <summary>
        /// Вычисляет площадь треугольника по координатам его вершин.
        /// </summary>
        /// <param name="v1">Первая вершина треугольника.</param>
        /// <param name="v2">Вторая вершина треугольника.</param>
        /// <param name="v3">Третья вершина треугольника.</param>
        /// <returns>Площадь треугольника как <see cref="double"/>.</returns>
        private double CalculateTriangleArea((double X, double Y) v1, (double X, double Y) v2, (double X, double Y) v3)
        {
            return Math.Abs((v1.X * (v2.Y - v3.Y) + v2.X * (v3.Y - v1.Y) + v3.X * (v1.Y - v2.Y)) / 2.0);
        }
    }
}