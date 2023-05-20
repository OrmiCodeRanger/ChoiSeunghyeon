"""
Given a sequence S, find the total length of LIS of every consecutive
subsequence (subsequence which elements are consecutive in the original
sequence) of S
with non zero length

수열 S가 주어졌을 때, 인접수열의 모든 LIS의 합을 구하세요. 인접수열이란 수열 S의
길이가 0이 아닌 부분수열인데 각각의 원소들이 서로 인접한 경우를 의미합니다.
"""
from bisect import bisect_left
from sys import stdin
from typing import Callable


def length_of_lis(iterable):
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
    """I don't want to use memory to store read values.
    This method itself is a iterator that calls `readline` each time
    until given count"""
    for _ in range(n):
        yield int(readline())


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        it = generator_for_readline(N, stdin.readline)
        ls = list(it)

        submit = 0

        # using two-pointer method to get all consecutive subsequence
        for left in range(len(ls)):
            for right in range(left, len(ls)):
                submit += length_of_lis(ls[left:right + 1])

        print(f'Case #{i}: {submit}')

# end main

