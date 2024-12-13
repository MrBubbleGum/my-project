using Microsoft.VisualStudio.TestTools.UnitTesting;
using ExamResultsLibrary;

namespace ExamResultsTests
{
    [TestClass]
    public class ExamModuleTest
    {
        public TestContext TestContext { get; set; }

        [TestInitialize]
        public void Setup()
        {
            // ���, ������� ���������� ����� ������ ������
        }

        [TestCleanup]
        public void Cleanup()
        {
            TestContext.WriteLine("���� ��������.");
        }

        [TestMethod]
        public void TestAverageScore()
        {
            var student1 = new ExamResult("Student A", 85);
            var student2 = new ExamResult("Student B", 95);
            double average = (student1.Score + student2.Score) / 2;
            Assert.AreEqual(90.0, average);
            TestContext.WriteLine("TestAverageScore �������� �������.");
        }

        [TestMethod]
        public void TestScoreDifference()
        {
            var student1 = new ExamResult("Student A", 85);
            var student2 = new ExamResult("Student B", 95);
            int difference = student1.Score - student2.Score;
            Assert.AreEqual(-10, difference);
            TestContext.WriteLine("TestScoreDifference �������� �������.");
        }

        [TestMethod]
        public void TestSumScores()
        {
            var student1 = new ExamResult("Student A", 70);
            var student2 = new ExamResult("Student B", 80);
            int sum = student1.Score + student2.Score;
            Assert.AreEqual(150, sum);
            TestContext.WriteLine("TestSumScores �������� �������.");
        }

        [TestMethod]
        public void TestNegativeScoreDifference()
        {
            var student1 = new ExamResult("Student A", 60);
            var student2 = new ExamResult("Student B", 75);
            int difference = student1.Score - student2.Score;
            Assert.AreEqual(-15, difference);
            TestContext.WriteLine("TestNegativeScoreDifference �������� �������.");
        }

        [TestMethod]
        public void TestEqualScores()
        {
            var student1 = new ExamResult("Student A", 88);
            var student2 = new ExamResult("Student B", 88);
            Assert.AreEqual(student1.Score, student2.Score);
            TestContext.WriteLine("TestEqualScores �������� �������.");
        }

        [TestMethod]
        public void TestHigherScore()
        {
            var student1 = new ExamResult("Student A", 92);
            var student2 = new ExamResult("Student B", 85);
            Assert.IsTrue(student1.Score > student2.Score);
            TestContext.WriteLine("TestHigherScore �������� �������.");
        }

        [TestMethod]
        public void TestLowerScore()
        {
            var student1 = new ExamResult("Student A", 78);
            var student2 = new ExamResult("Student B", 82);
            Assert.IsTrue(student1.Score < student2.Score);
            TestContext.WriteLine("TestLowerScore �������� �������.");
        }

        [TestMethod]
        public void TestNonZeroScore()
        {
            var student = new ExamResult("Student A", 67);
            Assert.AreNotEqual(0, student.Score);
            TestContext.WriteLine("TestNonZeroScore �������� �������.");
        }

        [TestMethod]
        public void TestMaxPossibleScore()
        {
            var student = new ExamResult("Student A", 100);
            Assert.AreEqual(100, student.Score);
            TestContext.WriteLine("TestMaxPossibleScore �������� �������.");
        }

        [TestMethod]
        public void TestMinPossibleScore()
        {
            var student = new ExamResult("Student A", 0);
            Assert.AreEqual(0, student.Score);
            TestContext.WriteLine("TestMinPossibleScore �������� �������.");
        }

        [TestMethod]
        public void TestScoreBoundaryAbove()
        {
            var student = new ExamResult("Student A", 101);
            Assert.IsTrue(student.Score > 100, "Score should not be greater than 100");
            TestContext.WriteLine("TestScoreBoundaryAbove �������� �������.");
        }

        [TestMethod]
        public void TestScoreBoundaryBelow()
        {
            var student = new ExamResult("Student A", -1);
            Assert.IsTrue(student.Score < 0, "Score should not be less than 0");
            TestContext.WriteLine("TestScoreBoundaryBelow �������� �������.");
        }

        [TestMethod]
        public void TestValidScoreRange()
        {
            var student = new ExamResult("Student A", 50);
            Assert.IsTrue(student.Score >= 0 && student.Score <= 100);
            TestContext.WriteLine("TestValidScoreRange �������� �������.");
        }

        [TestMethod]
        public void TestInvalidScore()
        {
            var student = new ExamResult("Student A", 110);
            Assert.IsTrue(student.Score > 100, "Score is invalid");
            TestContext.WriteLine("TestInvalidScore �������� �������.");
        }

        [TestMethod]
        public void TestZeroScore()
        {
            var student = new ExamResult("Student A", 0);
            Assert.AreEqual(0, student.Score);
            TestContext.WriteLine("TestZeroScore �������� �������.");
        }
    }
}