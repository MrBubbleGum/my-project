using System;
using System.Collections.Generic;
using System.Text;
using CarNumberExtractorLib;

namespace CarNumberExtractorConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            List<StringBuilder> reports = new List<StringBuilder>();

            Console.WriteLine("Введите отчёты о ДТП (введите пустую строку для завершения ввода):");

            while (true)
            {
                string input = Console.ReadLine();

                if (string.IsNullOrWhiteSpace(input))
                {
                    break;
                }

                reports.Add(new StringBuilder(input));
            }

            var extractor = new CarNumberExtractor();
            var carNumbers = extractor.ExtractCarNumbers(reports);

            Console.WriteLine("\nАвтомобильные номера и количество их упоминаний:");

            foreach (var carNumber in carNumbers)
            {
                Console.WriteLine($"{carNumber.Key}: {carNumber.Value}");
            }
        }
    }
}