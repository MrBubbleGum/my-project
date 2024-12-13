using System;
using ArrayLibrary;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введите размер первого массива:");
        int size1 = int.Parse(Console.ReadLine());
        int[] array1 = new int[size1];
        Console.WriteLine("Введите элементы первого массива:");
        for (int i = 0; i < size1; i++)
        {
            array1[i] = int.Parse(Console.ReadLine());
        }

        Console.WriteLine("Введите размер второго массива:");
        int size2 = int.Parse(Console.ReadLine());
        int[] array2 = new int[size2];
        Console.WriteLine("Введите элементы второго массива:");
        for (int i = 0; i < size2; i++)
        {
            array2[i] = int.Parse(Console.ReadLine());
        }

        OneDimensionalArray firstArray = new OneDimensionalArray(array1);
        OneDimensionalArray secondArray = new OneDimensionalArray(array2);

        Console.WriteLine($"Максимальный элемент первого массива: {firstArray.FindMax()}");
        Console.WriteLine($"Максимальный элемент второго массива: {secondArray.FindMax()}");

        if (firstArray.Length > secondArray.Length)
        {
            int minElement = secondArray.FindMax(); 
            for (int i = 0; i < secondArray.Length; i++)
            {
                firstArray[i] = minElement;
            }
        }

        Console.WriteLine("Первый массив после замены:");
        for (int i = 0; i < firstArray.Length; i++)
        {
            Console.Write(firstArray[i] + " ");
        }
    }
}