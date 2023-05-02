import unittest
from ex27212 import sol, normalise_index


class TestSolution(unittest.TestCase):

    def test_1(self):
        self.assertEqual(20, sol([[1, 10], [10, 10]],
                                 normalise_index([1, 2]),
                                 normalise_index([1, 2, 2])))

    def test_2(self):
        self.assertEqual(20, sol([[10, 1], [1, 10]],
                                 normalise_index([1, 2]),
                                 normalise_index([1, 2, 2])))

    def test_3(self):
        self.assertEqual(21, sol([[10, 1], [1, 1]],
                                 normalise_index([1, 2, 1]),
                                 normalise_index([1, 2, 1])))

    def test_4(self):
        self.assertEqual(100, sol(
            [
                [1, 1, 1],
                [1, 100, 1],
                [1, 1, 1]],
            [0, 0, 0, 0, 0, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))


if __name__ == "__main__":
    unittest.main()
# end main
