using System;
using System.Collections.Generic;
using System.Linq;

namespace TireShopLibrary
{
    /// <summary>
    /// Класс для управления всеми работами
    /// </summary>
    public class WorkManager
    {
        private List<Work> works;

        public WorkManager()
        {
            works = new List<Work>();
        }

        public void AddWork(Work work)
        {
            works.Add(work);
        }

        public Dictionary<string, double> GetAverageWorkCountPerCar()
        {
            return works.GroupBy(w => w.GetWorkType())
                        .ToDictionary(g => g.Key, g => g.Count() / (double)works.Select(w => w.Car).Distinct().Count());
        }

        public string GetMostFrequentWorkForCar(string car)
        {
            return works.Where(w => w.Car == car)
                        .GroupBy(w => w.GetWorkType())
                        .OrderByDescending(g => g.Count())
                        .FirstOrDefault()?.Key ?? "Нет данных";
        }

        public Dictionary<string, decimal> GetTotalCostByWorkType(DateTime startDate, DateTime endDate)
        {
            return works.Where(w => w.Date >= startDate && w.Date <= endDate)
                        .GroupBy(w => w.GetWorkType())
                        .ToDictionary(g => g.Key, g => g.Sum(w => w.Cost));
        }

        public void ApplyDiscount(string workType, decimal discountPercentage)
        {
            foreach (var work in works.Where(w => w.GetWorkType() == workType))
            {
                work.Cost -= work.Cost * discountPercentage / 100;
            }
        }

        public List<Work> GetWorks()
        {
            return works;
        }
    }
}