using System;

namespace TireShopLibrary
{
    /// <summary>
    /// Класс для работы "Балансировка колес"
    /// </summary>
    public class WheelBalancing : Work
    {
        public WheelBalancing(DateTime date, string car, decimal cost) : base(date, car, cost) { }

        public override string GetWorkType()
        {
            return "Балансировка колес";
        }
    }
}