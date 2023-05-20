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


def make_lis_cache(out_cache, num):
    """
    Args:
        out_cache (2d-list): cache for on-going LIS-cache of consecutive
        subsequence
        num (int): in-coming new element from sequence S
    """
    for cache in out_cache:
        idx = bisect_left(cache, num)
        if len(cache) == idx:
            cache.append(num)
        else:
            cache[idx] = num
    out_cache.append([num])


def solution(iterable):
    cache = []
    count = 0

    for num in iterable:
        make_lis_cache(cache, num)
        count += sum(len(x) for x in cache)

    # flatten 2-d cache
    return count


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

        submit = solution(it)

        print(f'Case #{i}: {submit}')

# end main

