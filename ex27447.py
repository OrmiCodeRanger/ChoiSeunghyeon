"""
boj.kr/27447

deque
"""
from sys import stdin
from collections import deque
from enum import Enum, auto

input = stdin.readline


class Ord(Enum):
    Less = auto()
    Greater = auto()
    Equal = auto()


def compare(lhs, rhs) -> Ord:
    if lhs < rhs:
        return Ord.Less
    if lhs > rhs:
        return Ord.Greater
    return Ord.Equal


def test(i: int, idx: int) -> bool:
    return (i >> idx) & 1 == 1


def set(i: int, idx: int) -> int:
    """
    turn on the bit of given index

    returns result integer which can be re-assigned to the origin.
    """
    i |= 1 << idx
    return i


def reset(i: int, idx: int) -> int:
    """
    turn off the bit of given index

    returns result integer which can be re-assigned to the origin.
    """
    i &= ~(1 << idx)
    return i


def is_customer_come(day, schedule_bitset) -> bool:
    return test(schedule_bitset, day)


def solution(M: int, schedule_bitset: int, schedule_deque: deque[int]) -> bool:

    last_time = schedule_deque[-1]
    bowl_cnt = 0
    coffee_cnt = 0

    for day in range(last_time + 1):
        delta_time = 1 << 31
        if len(schedule_deque) > 0:
            delta_time = schedule_deque[0] - day
        match (is_customer_come(day, schedule_bitset),
               compare(delta_time, M),
               bowl_cnt > 0,
               coffee_cnt > 0):
            case (True, _, _, True):
                # 사람이 와 있고 커피가 준비가 돼 있으면 서빙한다.
                coffee_cnt -= 1

            case (True, _, _, _):
                # Customer says, no coffee?? It's terrible!!!
                return False

            case (False, Ord.Greater, _, _):
                # 사람이 아직 안 와 있고, 커피 우릴 시간이 아직 안 돼 있으면 일단
                # 그릇부터 만들어 놓는다.
                bowl_cnt += 1

            case (False, Ord.Less | Ord.Equal, False, _):
                # 사람이 아직 안 와 있고, 커피 우릴 시간이 적당한데 그릇이 없으면
                # 일단 그릇부터 만들어 놓는다.
                bowl_cnt += 1

            case (False, Ord.Less | Ord.Equal, True, _):
                # 커피를 우린다. (그릇을 커피로 변환한다)
                coffee_cnt += 1
                bowl_cnt -= 1
                schedule_deque.popleft()

    return True


if __name__ == "__main__":
    N, M = [int(x) for x in input().split()]

    schedule_bitset = 0
    schedule_deque = deque[int]()

    for time in map(int, input().split()):
        last_time = time
        schedule_bitset = set(schedule_bitset, time)
        schedule_deque.append(time)

    print('success'
          if solution(M, schedule_bitset, schedule_deque)
          else 'fail')


# end main
