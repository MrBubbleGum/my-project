using System;

namespace TireShopLibrary
{
    /// <summary>
    /// Класс для работы "Ремонт проколов"
    /// </summary>
    public class PunctureRepair : Work
    {
        public PunctureRepair(DateTime date, string car, decimal cost) : base(date, car, cost) { }

        public override string GetWorkType()
        {
            return "Ремонт проколов";
        }
    }
}