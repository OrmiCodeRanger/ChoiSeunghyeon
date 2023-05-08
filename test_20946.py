import ex20946
import unittest
import random


class TestSolution(unittest.TestCase):

    def test_find_prime_1(self):
        self.assertEqual([], ex20946.find_prime(2))

    def test_find_prime_2(self):
        self.assertEqual([], ex20946.find_prime(3))

    def test_find_prime_3(self):
        self.assertEqual([2, 2, 2, 3], ex20946.find_prime(24))

    def test_find_prime_timeout(self):
        ex20946.find_prime(random.randint(2, 10 ** 12))

    def test_sol_timeout(self):
        ex20946.solution(random.randint(2, 10 ** 12))
