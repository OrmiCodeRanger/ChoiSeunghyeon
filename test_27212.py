from ex27212 import sol


def test_1():
    assert 20 == sol([[1, 10], [10, 10]], [1, 2], [1, 2, 2])


def test_2():
    assert 20 == sol([[10, 1], [1, 10]], [1, 2], [1, 2, 2])
