import unittest
from ex11066 import solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        k = [40, 30, 30, 50]
        self.assertEqual(300, solution(k))
    # end def

    def test_2(self):
        k = [1, 21, 3, 4, 5, 35, 5, 4, 3, 5, 98, 21, 14, 17, 32]
        answer = 864
        self.assertEqual(answer, solution(k))
    # end def


if __name__ == "__main__":
    unittest.main()
# end main
