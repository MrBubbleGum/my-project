using System;

namespace ExamResultsLibrary
{
    /// <summary>
    /// Класс для хранения информации о результатах сдачи экзамена.
    /// </summary>
    public class ExamResult
    {
        public string StudentName { get; }
        public int Score { get; }

        public ExamResult(string studentName, int score)
        {
            StudentName = studentName;
            Score = score;
        }

        /// <summary>
        /// Перегрузка оператора сложения для суммирования оценок двух студентов.
        /// </summary>
        public static double operator +(ExamResult a, ExamResult b)
        {
            return (a.Score + b.Score) / 2.0; // Возвращает средний балл
        }

        /// <summary>
        /// Перегрузка оператора вычитания для нахождения разности оценок двух студентов.
        /// </summary>
        public static int operator -(ExamResult a, ExamResult b)
        {
            return a.Score - b.Score; // Возвращает разность оценок
        }
    }
}