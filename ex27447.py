"""
boj.kr/27447

deque
"""
from sys import stdin
from collections import deque
from enum import Enum, auto

input = stdin.readline

MAX_DAY = 1_000_000
BIT_CNT = 32
BIN_CNT = MAX_DAY // BIT_CNT


class Ord(Enum):
    Less = auto()
    Greater = auto()
    Equal = auto()


def bin_no(idx) -> int:
    return idx // BIN_CNT


def bit_no(idx) -> int:
    return idx % BIN_CNT


class Bitset:

    def __init__(self):
        self.bits = [0 for _ in range(MAX_DAY + 1)]

    def test(self, idx) -> bool:
        return self.bits[bin_no(idx)] >> bit_no(idx) & 1 == 1

    def set(self, idx):
        self.bits[bin_no(idx)] |= (1 << bit_no(idx))

    def reset(self, idx):
        self.bits[bin_no(idx)] &= ~(1 << bit_no(idx))


# test code
# bs = Bitset()

# bit = 10
# bs.set(bit)
# assert bs.test(bit)
# bs.reset(bit)
# assert not bs.test(bit)

# bit = 1_000_000_000
# bs.set(bit)
# assert bs.test(bit)
# bs.reset(bit)
# assert not bs.test(bit)


def compare(lhs, rhs) -> Ord:
    if lhs < rhs:
        return Ord.Less
    if lhs > rhs:
        return Ord.Greater
    return Ord.Equal


def solution(M: int, bitset: Bitset, schedule: deque[int]) -> bool:

    last_time = schedule[-1]
    bowl_cnt = 0
    coffee_cnt = 0

    for day in range(last_time + 1):
        delta_time = 1 << 31
        if len(schedule) > 0:
            delta_time = schedule[0] - day
        match (bitset.test(day),  # does customer come?
               compare(delta_time, M),  # is it right time to brew a coffee?
               bowl_cnt > 0,
               coffee_cnt > 0):
            case (True, _, _, True):
                # 사람이 와 있고 커피가 준비가 돼 있으면 서빙한다.
                coffee_cnt -= 1

            case (True, _, _, False):
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
                schedule.popleft()

            case _:
                raise RuntimeError('Unknown arm has detected!')

    return True


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())

    schedule_bitset = Bitset()
    schedule_deque = deque[int]()

    for time in map(int, input().rstrip().split()):
        schedule_bitset.set(time)
        schedule_deque.append(time)

    print('success'
          if solution(M, schedule_bitset, schedule_deque)
          else 'fail')


# end main
