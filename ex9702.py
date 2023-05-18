from bisect import bisect_left
from sys import stdin
from typing import Callable, Iterator

input = stdin.readline


def length_of_lis(iterable: Iterator):
    """lower bound를 활용한 효율적인 캐시 검색"""
    cache = []

    for num in iterable:
        newL = bisect_left(cache, num)
        if len(cache) == newL:
            cache.append(num)
        else:
            cache[newL] = num

    return len(cache)


def generator_for_readline(n: int, readline: Callable):
    for _ in range(n):
        yield int(readline())


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        it = generator_for_readline(N, input)
        submit = length_of_lis(it)

        print(f'Case #{i}: {submit}')

# end main
