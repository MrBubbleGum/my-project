using Microsoft.VisualStudio.TestTools.UnitTesting;
using WordPermutations;
using System.Collections.Generic;
using WordPermutations.Logic;

namespace WordPermutations
{
    [TestClass]
    public class PermutationServiceTests
    {
        [TestMethod]
        public void TestSingleWord()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("hello");

            Assert.AreEqual(1, result.Count);
            CollectionAssert.Contains(result, "hello");
        }

        [TestMethod]
        public void TestTwoWords()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("hello_world");

            Assert.AreEqual(2, result.Count);
            CollectionAssert.Contains(result, "hello world");
            CollectionAssert.Contains(result, "world hello");
        }

        [TestMethod]
        public void TestThreeWords()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("one_two_three");

            Assert.AreEqual(6, result.Count);
            CollectionAssert.Contains(result, "one two three");
            CollectionAssert.Contains(result, "one three two");
            CollectionAssert.Contains(result, "two one three");
            CollectionAssert.Contains(result, "two three one");
            CollectionAssert.Contains(result, "three one two");
            CollectionAssert.Contains(result, "three two one");
        }

        [TestMethod]
        public void TestEmptyString()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("");

            Assert.AreEqual(1, result.Count);
            CollectionAssert.Contains(result, "");
        }

        [TestMethod]
        public void TestDuplicateWords()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("cat_cat");

            Assert.AreEqual(2, result.Count);
            CollectionAssert.Contains(result, "cat cat");
        }

        [TestMethod]
        public void TestFourWords()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("apple_banana_orange_grape");

            Assert.AreEqual(24, result.Count);
        }

        [TestMethod]
        public void TestFiveWords()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("one_two_three_four_five");

            Assert.AreEqual(120, result.Count);  // 5! = 120 permutations
        }

        [TestMethod]
        public void TestWithSpecialCharacters()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("hello_world!");

            Assert.AreEqual(2, result.Count);
            CollectionAssert.Contains(result, "hello world!");
            CollectionAssert.Contains(result, "world! hello");
        }

        [TestMethod]
        public void TestWithNumbers()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("1_2_3");

            Assert.AreEqual(6, result.Count);  // 3!
        }

        [TestMethod]
        public void TestCaseSensitivity()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("Hello_world");

            Assert.AreEqual(2, result.Count);
            CollectionAssert.Contains(result, "Hello world");
            CollectionAssert.Contains(result, "world Hello");
        }

        [TestMethod]
        public void TestWhitespaceHandling()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("one_ two_ three ");

            Assert.AreEqual(6, result.Count);
            CollectionAssert.Contains(result, "one  two  three ");
        }

        [TestMethod]
        public void TestLongSentence()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("long_sentence_with_many_words");

            // Проверяем, что результат содержит хотя бы одну перестановку
            CollectionAssert.Contains(result, "long sentence with many words");
        }

        [TestMethod]
        public void TestOnlyUnderscore()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("_");

            Assert.AreEqual(1, result.Count);  // Пустая строка, так как нет слов
        }

        [TestMethod]
        public void TestWithPunctuation()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations("hello_world!");

            CollectionAssert.Contains(result, "hello world!");
        }

        [TestMethod]
        public void TestTwoWordsWithSpacesAroundUnderscore()
        {
            var sentencePermutations = new PermutationService();
            var result = sentencePermutations.GetPermutations(" hello _world ");

            Assert.AreEqual(2, result.Count);
            CollectionAssert.Contains(result, " hello  world ");
        }
    }
}