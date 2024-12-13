using Microsoft.VisualStudio.TestTools.UnitTesting;
using GeometryLibrary;
using System.Drawing;

namespace GeometryLibrary.Tests
{
    [TestClass]
    public class GeometryTests
    {
        [TestMethod]
        public void TestRectangleArea()
        {
            var rectangle = new Rectangle(new (double, double)[] { (0, 0), (2, 0), (2, 3), (0, 3) });
            Assert.AreEqual(6, rectangle.CalculateArea());
        }

        [TestMethod]
        public void TestTriangleArea()
        {
            var triangle = new Triangle(new (double, double)[] { (0, 0), (4, 0), (0, 3) });
            Assert.AreEqual(6, triangle.CalculateArea());
        }

        [TestMethod]
        public void TestCircleArea()
        {
            var circle = new Circle((0, 0), 2);
            Assert.AreEqual(Math.PI * 4, circle.CalculateArea(), 0.0001);
        }
    }
}