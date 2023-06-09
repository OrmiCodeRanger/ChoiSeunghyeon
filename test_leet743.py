import leet743


def do_test(times, n, k, answer):
    assert answer == leet743.Solution().networkDelayTime(times, n, k)


class TestClass:
    def test_1(self):
        do_test([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2)

    def test_2(self):
        do_test(times=[[1, 2, 1]], n=2, k=1, answer=1)

    def test_3(self):
        do_test(times=[[1, 2, 1]], n=2, k=2, answer=-1)

    def test_4(self):
        do_test(
            times=[
                [2, 4, 10],
                [5, 2, 38],
                [3, 4, 33],
                [4, 2, 76],
                [3, 2, 64],
                [1, 5, 54],
                [1, 4, 98],
                [2, 3, 61],
                [2, 1, 0],
                [3, 5, 77],
                [5, 1, 34],
                [3, 1, 79],
                [5, 3, 2],
                [1, 2, 59],
                [4, 3, 46],
                [5, 4, 44],
                [2, 5, 89],
                [4, 5, 21],
                [1, 3, 86],
                [4, 1, 95],
            ],
            n=5,
            k=1,
            answer=69,
        )
