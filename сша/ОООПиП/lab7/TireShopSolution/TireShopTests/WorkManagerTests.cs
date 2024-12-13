using System;
using TireShopLibrary;
using Xunit;

namespace TireShopTests
{
    public class WorkManagerTests
    {
        [Fact]
        public void TestAverageWorkCountPerCar()
        {
            var manager = new WorkManager();
            manager.AddWork(new TireReplacement(DateTime.Now, "Toyota", 500));
            manager.AddWork(new PunctureRepair(DateTime.Now, "Toyota", 300));
            manager.AddWork(new WheelBalancing(DateTime.Now, "Honda", 200));
            manager.AddWork(new TireReplacement(DateTime.Now, "Honda", 500));

            var averageWorks = manager.GetAverageWorkCountPerCar();

            Assert.Equal(1.0, averageWorks["Замена шин"]);
            Assert.Equal(0.5, averageWorks["Балансировка колес"]);
        }

        [Fact]
        public void TestMostFrequentWorkForCar()
        {
            var manager = new WorkManager();
            manager.AddWork(new TireReplacement(DateTime.Now, "Toyota", 500));
            manager.AddWork(new PunctureRepair(DateTime.Now, "Toyota", 300));
            manager.AddWork(new WheelBalancing(DateTime.Now, "Toyota", 200));
            manager.AddWork(new TireReplacement(DateTime.Now, "Toyota", 500));

            var mostFrequentWork = manager.GetMostFrequentWorkForCar("Toyota");

            Assert.Equal("Замена шин", mostFrequentWork);
        }

        [Fact]
        public void TestTotalCostByWorkType()
        {
            var manager = new WorkManager();
            manager.AddWork(new TireReplacement(DateTime.Now, "Toyota", 500));
            manager.AddWork(new PunctureRepair(DateTime.Now, "Toyota", 300));
            manager.AddWork(new WheelBalancing(DateTime.Now, "Toyota", 200));
            manager.AddWork(new TireReplacement(DateTime.Now, "Honda", 500));

            var totalCosts = manager.GetTotalCostByWorkType(DateTime.Now.AddDays(-1), DateTime.Now.AddDays(1));

            Assert.Equal(1000, totalCosts["Замена шин"]);
            Assert.Equal(300, totalCosts["Ремонт проколов"]);
        }

        [Fact]
        public void TestApplyDiscount()
        {
            var manager = new WorkManager();
            manager.AddWork(new TireReplacement(DateTime.Now, "Toyota", 500));
            manager.AddWork(new PunctureRepair(DateTime.Now, "Toyota", 300));

            manager.ApplyDiscount("Замена шин", 10);

            var totalCosts = manager.GetTotalCostByWorkType(DateTime.Now.AddDays(-1), DateTime.Now.AddDays(1));

            Assert.Equal(450, totalCosts["Замена шин"]);  // 10% скидка
        }
    }
}