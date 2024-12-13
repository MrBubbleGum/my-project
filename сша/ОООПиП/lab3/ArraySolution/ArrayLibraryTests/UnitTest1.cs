using Microsoft.VisualStudio.TestTools.UnitTesting;
using ArrayLibrary;

namespace ArrayLibraryTests
{
    [TestClass]
    public class OneDimensionalArrayTests
    {
        [TestMethod]
        public void TestFindMax()
        {
            var array = new OneDimensionalArray(new[] { 1, 2, 3, 4, 5 });
            Assert.AreEqual(5, array.FindMax());
        }

        [TestMethod]
        public void TestCountGreaterThanLength()
        {
            var array = new OneDimensionalArray(new[] { 1, 6, 3, 8 });
            Assert.AreEqual(2, array.CountGreaterThanLength());
        }

        // Добавьте больше тестов для других методов
    }
}