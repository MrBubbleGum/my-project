using System;

namespace ArrayLibrary
{
    /// <summary>
    /// Класс, представляющий одномерный массив целых чисел.
    /// </summary>
    public class OneDimensionalArray
    {
        private int[] _array;

        /// <summary>
        /// Конструктор, принимающий массив целых чисел.
        /// </summary>
        /// <param name="array">Массив целых чисел.</param>
        public OneDimensionalArray(int[] array)
        {
            _array = array ?? throw new ArgumentNullException(nameof(array));
        }

        /// <summary>
        /// Свойство для получения длины массива.
        /// </summary>
        public int Length => _array.Length;

        /// <summary>
        /// Индикатор для доступа к элементам массива.
        /// </summary>
        /// <param name="index">Индекс элемента.</param>
        /// <returns>Элемент массива по указанному индексу.</returns>
        public int this[int index]
        {
            get => _array[index];
            set => _array[index] = value;
        }

        /// <summary>
        /// Метод для поиска максимального элемента в массиве.
        /// </summary>
        /// <returns>Максимальный элемент.</returns>
        public int FindMax()
        {
            if (_array.Length == 0) throw new InvalidOperationException("Array is empty.");
            int max = _array[0];
            foreach (var item in _array)
            {
                if (item > max) max = item;
            }
            return max;
        }

        /// <summary>
        /// Метод для поиска максимального элемента в заданном диапазоне индексов.
        /// </summary>
        /// <param name="start">Начальный индекс.</param>
        /// <param name="end">Конечный индекс.</param>
        /// <returns>Максимальный элемент в заданном диапазоне.</returns>
        public int FindMaxInRange(int start, int end)
        {
            if (start < 0 || end >= _array.Length || start > end)
                throw new ArgumentOutOfRangeException("Invalid index range.");

            int max = _array[start];
            for (int i = start; i <= end; i++)
            {
                if (_array[i] > max) max = _array[i];
            }
            return max;
        }

        /// <summary>
        /// Метод, возвращающий количество элементов, больших длины массива.
        /// </summary>
        /// <returns>Количество элементов больше длины массива.</returns>
        public int CountGreaterThanLength()
        {
            int count = 0;
            foreach (var item in _array)
            {
                if (item > Length) count++;
            }
            return count;
        }

        /// <summary>
        /// Метод, возвращающий количество элементов, меньших длины массива.
        /// </summary>
        /// <returns>Количество элементов меньше длины массива.</returns>
        public int CountLessThanLength()
        {
            int count = 0;
            foreach (var item in _array)
            {
                if (item < Length) count++;
            }
            return count;
        }

        /// <summary>
        /// Переопределение оператора равенства для сравнения объектов.
        /// </summary>
        public static bool operator ==(OneDimensionalArray a, OneDimensionalArray b)
        {
            if (ReferenceEquals(a, b)) return true;
            if (ReferenceEquals(a, null) || ReferenceEquals(b, null)) return false;
            return a.Length == b.Length && a.Equals(b._array);
        }

        public static bool operator !=(OneDimensionalArray a, OneDimensionalArray b)
        {
            return !(a == b);
        }

        public override bool Equals(object obj)
        {
            if (obj is OneDimensionalArray other)
            {
                if (Length != other.Length) return false;
                for (int i = 0; i < Length; i++)
                {
                    if (_array[i] != other._array[i]) return false;
                }
                return true;
            }
            return false;
        }

        public override int GetHashCode()
        {
            return HashCode.Combine(_array);
        }
    }
}