using System;
using WordPermutations.Logic;

namespace WordPermutations
{
    class Program
    {
        public void Start()
        {
            Console.WriteLine("Введите предложение, разделенное символом подчеркивания (_): ");
            string input = Console.ReadLine();

           PermutationService permutator = new PermutationService();
            var permutations = permutator.GetPermutations(input);

            Console.WriteLine("Все возможные перестановки:");
            foreach (var permutation in permutations)
            {
                Console.WriteLine(permutation);
            }
        }
    }
}