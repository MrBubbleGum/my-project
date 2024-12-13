import unittest
from unittest.mock import patch
from io import StringIO

from who import kod, arry, sch 
class TestSearchFunctions(unittest.TestCase):

    def test_kod(self):
    
        self.assertEqual(kod([1, 2, 3, 4, 5], 3), 2)  # 3 находится в индексе 2 (0-based)
        self.assertEqual(kod([1, 2, 3, 4, 5], 6), -1)  # 6 не найдено
        self.assertEqual(kod([1, 2, 3], 1), 0)  # 1 находится в индексе 0
        self.assertEqual(kod([1, 2, 3], 2), 1)  # 2 находится в индексе 1
        self.assertEqual(kod([1, 2, 3], 4), -1)  # 4 не найдено

    @patch('builtins.input', side_effect=[5, 1, 2, 3, 4, 5])
    def test_arry(self, mock_input):
        arr = arry()  # Симулируем ввод
        self.assertEqual(arr, [1, 2, 3, 4, 5])  # Проверяем, что массив правильно заполнился


    @patch('builtins.input', side_effect=[5, 1, 2, 3, 4, 5, 3])  # Вводим массив и искомое число 3
    @patch('sys.stdout', new_callable=StringIO)  # Перехватываем вывод
    def test_sch_found(self, mock_stdout, mock_input):
        sch()  # Вызываем функцию sch
        output = mock_stdout.getvalue().strip()  # Получаем вывод
        self.assertEqual(output, "элемент в позиции 3")  # Проверяем, что вывод правильный

    @patch('builtins.input', side_effect=[5, 1, 2, 3, 4, 5, 6])  # Вводим массив и искомое число 6
    @patch('sys.stdout', new_callable=StringIO)  # Перехватываем вывод
    def test_sch_not_found(self, mock_stdout, mock_input):
        sch()  # Вызываем функцию sch
        output = mock_stdout.getvalue().strip()  # Получаем вывод
        self.assertEqual(output, "элемент не найден")  # Проверяем, что вывод правильный

if __name__ == '__main__':
    unittest.main()