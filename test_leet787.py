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
