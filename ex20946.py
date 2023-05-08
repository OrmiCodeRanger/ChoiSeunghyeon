"""boj.kr/20946 합성인수분해

i) N이 소수이면 -1을 리턴한다. ===> 소수판별 in O(sqrt(N))
ii) N을 소인수분해하여 수열 A를 만든다.
    1. N을 소인수분해하여 나온 원소들을 정렬한 수열 S를 구한다.
    2. S의 마지막 원소인 N을 제거한다.
    3. zip(S[:], S[1:])의 결과를 A에 넣는다.
    4. 만약 A의 마지막 원소가 소수라면, 그 다음 마지막 원소와 곱하여 A를 완성시킨다.
"""
from math import sqrt


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


def find_prime(n: int) -> list[int]:
    '''
    소인수분해를 수행하는 코드
    1. i=2로 시작하여 n % i == 0인지 확인한다.
    2. 만약 그렇다면 n % i != 0일때까지 다음을 반복한다.
        1. list에 i를 추가한다.
        2. n을 i로 나눈 몫으로 갱신한다.
    3. i를 다음 소인수로 설정한다.
    '''
    ret = []
    for i in range(2, int(sqrt(n))):
        if not is_prime(i):
            continue
        while n % i == 0:
            ret.append(i)
            n //= i

    return ret


def solution(n: int) -> list[int] | None:
    factorized = find_prime(n)
    if len(factorized) == 1:
        return None

    ret = list(map(lambda z: z[0] * z[1],
               zip(factorized[0::2], factorized[1::2])))

    # exception: last element might not inserted
    if len(factorized) % 2 != 0:
        ret.append(factorized[-1])

    if is_prime(ret[-1]):
        last = ret[-1]
        ret.pop()
        ret[-1] *= last
    return ret


if __name__ == "__main__":
    n = int(input())
    result = solution(n)
    if result is None or len(result) == 1:
        print(-1)
        quit()
    for e in result:
        print(e, end=' ')
    print()


# end main
