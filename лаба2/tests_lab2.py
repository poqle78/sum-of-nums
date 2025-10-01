import unittest
from лаба2.lab2 import *


# Тест функций
class Tests(unittest.TestCase):
    # Тест первой функции для нечетного количества элементов списка.
    def test1_odd_num_of_elems(self):
        self.assertEqual(fast_guess_num(37, [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]), [37, 3])

    # Тест первой функции для четного количества элементов списка.
    def test1_even_num_of_elems(self):
        self.assertEqual(fast_guess_num(37, [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]), [37, 3])

    # Тест первой функции поиска левого числа списка.
    def test1_left_edge(self):
        self.assertEqual(fast_guess_num(1, [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]), [1, 3])

    # Тест первой функции поиска правого числа списка.
    def test1_right_edge(self):
        self.assertEqual(fast_guess_num(59, [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]), [59, 4])

    # Тест функций со списком, состоящим из 1 элемента
    def test_1_elem(self):
        self.assertEqual(fast_guess_num(59, [59]), [59, 1])
        self.assertEqual(guess_num(59, [59]), [59, 1])

    # Тест второй функции
    def test2(self):
        self.assertEqual(guess_num(37, [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]), [37, 12])

    # Тест второй функции поиска левого числа списка.
    def test2_left_edge(self):
        self.assertEqual(guess_num(1, [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]), [1, 1])

    # Тест второй функции поиска правого числа списка.
    def test2_right_edge(self):
        self.assertEqual(guess_num(59, [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]), [59, 17])


if __name__ == '__main__':
    unittest.main()
