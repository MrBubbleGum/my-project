using System;
using System.Collections.Generic;
using System.Linq;

namespace WordPermutations.Logic
{
    public class PermutationService
    {
        // Метод, который генерирует все перестановки слов
        public List<string> GetPermutations(string sentence)
        {
            if (string.IsNullOrWhiteSpace(sentence.Replace("_", "")))
            {
                return new List<string> { "" };
            }

            string[] words = sentence.Split('_');
            var result = new List<string>();
            Permute(words, 0, words.Length - 1, result);
            return result;
        }

        // Рекурсивный метод для генерации перестановок
        private void Permute(string[] words, int l, int r, List<string> result)
        {
            if (l == r)
            {
                result.Add(string.Join(" ", words));
            }
            else
            {
                for (int i = l; i <= r; i++)
                {
                    Swap(ref words[l], ref words[i]);
                    Permute(words, l + 1, r, result);
                    Swap(ref words[l], ref words[i]); // Обратный swap для возврата начального состояния
                }
            }
        }

        // Метод для свапа двух элементов массива
        private void Swap(ref string a, ref string b)
        {
            string temp = a;
            a = b;
            b = temp;
        }
    }
}