using System;
using ExamResultsLibrary;

class Program
{
    /// <summary>
    /// Основной класс программы для ввода и обработки результатов экзаменов.
    /// </summary>
    static void Main()
    {
        Console.WriteLine("Введите имя студента и его оценку:");
        string name = Console.ReadLine();
        int score = int.Parse(Console.ReadLine());

        ExamResult student1 = new ExamResult(name, score);

        Console.WriteLine("Введите имя второго студента и его оценку:");
        string name2 = Console.ReadLine();
        int score2 = int.Parse(Console.ReadLine());

        ExamResult student2 = new ExamResult(name2, score2);

        // Вычисление среднего балла
        double averageScore = student1 + student2;
        Console.WriteLine($"Средний балл: {averageScore}");

        // Вычисление разности оценок
        int scoreDifference = student1 - student2;
        Console.WriteLine($"Разность оценок: {scoreDifference}");
    }
}