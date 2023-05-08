"""
boj.kr/11653

소인수 분해... 분해!!! 분하다 분해!!!
[ex20946.py] 문제를 풀다가 연속된 실패에 좌절감을 느끼던 찰나, 친구가 슬쩍 문제를 하나 건네주었다.
"""


def is_prime(n: int) -> bool:
    """
    Return True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for i in range(5, int(n**0.5)+1, 6):
            if n % i == 0 or n % (i+2) == 0:
                return False
        return True


def prime_factorize(n: int) -> list[int]:
    if n == 1:
        return []
    if is_prime(n):
        return [n, ]

    ret = []

    range_start = 2
    range_end = int(n ** 0.5) + 1

    for i in range(range_start, range_end):
        if not is_prime(i):
            continue
        while n % i == 0:
            ret.append(i)
            n //= i
        # end while

    # corner case: n is not 1
    if n != 1:
        ret.append(n)

    return ret


if __name__ == "__main__":
    n = int(input())
    for e in prime_factorize(n):
        print(e)
# end main
