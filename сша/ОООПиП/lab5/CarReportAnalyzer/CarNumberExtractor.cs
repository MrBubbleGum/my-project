using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using System.Linq;
using System.Text;

namespace CarNumberExtractorLib
{
    /// <summary>
    /// Класс для извлечения и подсчета автомобильных номеров из текстовых строк.
    /// </summary>
    public class CarNumberExtractor
    {
        // Регулярное выражение для поиска автомобильных номеров (пример для российских номеров)
        private static readonly Regex CarNumberRegex = new Regex(@"\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b", RegexOptions.Compiled);

        /// <summary>
        /// Извлекает и группирует автомобильные номера по количеству их упоминаний в отчётах.
        /// </summary>
        /// <param name="reports">Список строковых отчётов о ДТП.</param>
        /// <returns>Словарь, где ключ — автомобильный номер, а значение — количество его упоминаний.</returns>
        public Dictionary<string, int> ExtractCarNumbers(List<StringBuilder> reports)
        {
            var result = new Dictionary<string, int>();

            foreach (var report in reports)
            {
                // Поиск всех номеров в отчёте
                var matches = CarNumberRegex.Matches(report.ToString());

                foreach (Match match in matches)
                {
                    string carNumber = match.Value;

                    // Увеличиваем счётчик для каждого номера
                    if (result.ContainsKey(carNumber))
                    {
                        result[carNumber]++;
                    }
                    else
                    {
                        result[carNumber] = 1;
                    }
                }
            }

            return result;
        }
    }
}