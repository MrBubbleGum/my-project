using System;

namespace TireShopLibrary
{
    /// <summary>
    /// Базовый класс для всех видов работ
    /// </summary>
    public abstract class Work
    {
        public DateTime Date { get; set; }
        public string Car { get; set; }
        public decimal Cost { get; set; }

        public Work(DateTime date, string car, decimal cost)
        {
            Date = date;
            Car = car;
            Cost = cost;
        }

        public abstract string GetWorkType();
    }
}