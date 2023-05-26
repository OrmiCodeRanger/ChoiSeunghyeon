import leet787


def do_test(
    n: int, flights: list[list[int]], src: int, dst: int, k: int, answer: int
):
    assert answer == leet787.Solution().findCheapestPrice(
        n, flights, src, dst, k
    )


class TestClass:
    def test_1(self):
        do_test(
            n=3,
            flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]],
            src=0,
            dst=2,
            k=1,
            answer=200,
        )

    def test_2(self):
        do_test(
            n=3,
            flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]],
            src=0,
            dst=2,
            k=0,
            answer=500,
        )

    def test_3(self):
        do_test(
            n=4,
            flights=[
                [0, 1, 100],
                [1, 2, 100],
                [2, 0, 100],
                [1, 3, 600],
                [2, 3, 200],
            ],
            src=0,
            dst=3,
            k=1,
            answer=700,
        )

    def test_4(self):
        do_test(
            n=4,
            flights=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]],
            src=0,
            dst=3,
            k=1,
            answer=6,
        )
