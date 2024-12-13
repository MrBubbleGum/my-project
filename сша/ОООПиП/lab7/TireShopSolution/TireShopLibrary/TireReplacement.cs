using System;

namespace TireShopLibrary
{
    /// <summary>
    /// Класс для работы "Замена шин"
    /// </summary>
    public class TireReplacement : Work
    {
        public TireReplacement(DateTime date, string car, decimal cost) : base(date, car, cost) { }

        public override string GetWorkType()
        {
            return "Замена шин";
        }
    }
}