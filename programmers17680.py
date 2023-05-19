"""https://school.programmers.co.kr/learn/courses/30/lessons/17680
캐시 (LRU) 알고리즘
"""

from collections import deque


CACHE_HIT = 1
CACHE_MISS = 5


def solution(cachesize, cities):

    ls = [''] * cachesize
    cache = deque(ls, maxlen=cachesize)

    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            answer += CACHE_HIT
        else:
            answer += CACHE_MISS

        cache.append(city)
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork",
      "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju",
      "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))

print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))

print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))

print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))

print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
