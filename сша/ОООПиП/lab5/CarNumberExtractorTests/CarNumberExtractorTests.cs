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
        /// ���� ���������, ��� ����� ExtractCarNumbers ���������� ���������� ��������� ��� ������� �������� �������.
        /// </summary>
        [TestMethod]
        public void ExtractCarNumbers_ShouldReturnCorrectCount_WhenValidReports()
        {
            // Arrange
            var extractor = new CarNumberExtractor();
            var reports = new List<StringBuilder>
            {
                new StringBuilder("��������� ��� � ����������� �123��77 � ����������� �456��99."),
                new StringBuilder("���������� �123��77 ����� ����� � ���."),
                new StringBuilder("���������� �789��77 ��� ������� �� ����� ���.")
            };

            // Act
            var result = extractor.ExtractCarNumbers(reports);

            // Assert
            Assert.AreEqual(2, result["�123��77"], "���������� ���������� ������ �123��77 ������ ���� 2.");
            Assert.AreEqual(1, result["�456��99"], "���������� ���������� ������ �456��99 ������ ���� 1.");
            Assert.AreEqual(1, result["�789��77"], "���������� ���������� ������ �789��77 ������ ���� 1.");
        }

        /// <summary>
        /// ���� ���������, ��� ����� ExtractCarNumbers ���������� ������ �������, ���� ��� �������.
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
            Assert.AreEqual(0, result.Count, "��������� ������ ���� ������ �������, ���� ������� ���.");
        }

        /// <summary>
        /// ���� ���������, ��� ����� ExtractCarNumbers ���������� ������ �������, ���� � ������� ��� ������� �����������.
        /// </summary>
        [TestMethod]
        public void ExtractCarNumbers_ShouldReturnEmptyDictionary_WhenNoCarNumbers()
        {
            // Arrange
            var extractor = new CarNumberExtractor();
            var reports = new List<StringBuilder>
            {
                new StringBuilder("��������� ��� �� �����������, �� ������ �� ���� �������.")
            };

            // Act
            var result = extractor.ExtractCarNumbers(reports);

            // Assert
            Assert.AreEqual(0, result.Count, "��������� ������ ���� ������ �������, ���� � ������� ��� ������� �����������.");
        }
    }
}