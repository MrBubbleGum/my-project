using Microsoft.VisualStudio.TestTools.UnitTesting;
using CarNumberExtractorLib;
using System.Collections.Generic;
using System.Text;

namespace CarNumberExtractorTests
{
    [TestClass]
    public class CarNumberExtractorTests
    {
        /// <summary>
        /// Тест проверяет, что метод ExtractCarNumbers возвращает правильный результат при наличии валидных отчётов.
        /// </summary>
        [TestMethod]
        public void ExtractCarNumbers_ShouldReturnCorrectCount_WhenValidReports()
        {
            // Arrange
            var extractor = new CarNumberExtractor();
            var reports = new List<StringBuilder>
            {
                new StringBuilder("Произошло ДТП с автомобилем А123ВС77 и автомобилем К456ОР99."),
                new StringBuilder("Автомобиль А123ВС77 снова попал в ДТП."),
                new StringBuilder("Автомобиль М789КН77 был замечен на месте ДТП.")
            };

            // Act
            var result = extractor.ExtractCarNumbers(reports);

            // Assert
            Assert.AreEqual(2, result["А123ВС77"], "Количество упоминаний номера А123ВС77 должно быть 2.");
            Assert.AreEqual(1, result["К456ОР99"], "Количество упоминаний номера К456ОР99 должно быть 1.");
            Assert.AreEqual(1, result["М789КН77"], "Количество упоминаний номера М789КН77 должно быть 1.");
        }

        /// <summary>
        /// Тест проверяет, что метод ExtractCarNumbers возвращает пустой словарь, если нет отчётов.
        /// </summary>
        [TestMethod]
        public void ExtractCarNumbers_ShouldReturnEmptyDictionary_WhenNoReports()
        {
            // Arrange
            var extractor = new CarNumberExtractor();
            var reports = new List<StringBuilder>();

            // Act
            var result = extractor.ExtractCarNumbers(reports);

            // Assert
            Assert.AreEqual(0, result.Count, "Результат должен быть пустым словарём, если отчётов нет.");
        }

        /// <summary>
        /// Тест проверяет, что метод ExtractCarNumbers возвращает пустой словарь, если в отчётах нет номеров автомобилей.
        /// </summary>
        [TestMethod]
        public void ExtractCarNumbers_ShouldReturnEmptyDictionary_WhenNoCarNumbers()
        {
            // Arrange
            var extractor = new CarNumberExtractor();
            var reports = new List<StringBuilder>
            {
                new StringBuilder("Произошло ДТП на перекрестке, но номера не были указаны.")
            };

            // Act
            var result = extractor.ExtractCarNumbers(reports);

            // Assert
            Assert.AreEqual(0, result.Count, "Результат должен быть пустым словарём, если в отчётах нет номеров автомобилей.");
        }
    }
}