"""boj.kr/20946 합성인수분해

i) N이 소수이면 -1을 리턴한다. ===> 소수판별 in O(sqrt(N))
ii) N을 소인수분해하여 수열 A를 만든다.
    1. N을 소인수분해하여 나온 원소들을 정렬한 수열 S를 구한다.
    2. S의 마지막 원소인 N을 제거한다.
    3. zip(S[:], S[1:])의 결과를 A에 넣는다.
    4. 만약 A의 마지막 원소가 소수라면, 그 다음 마지막 원소와 곱하여 A를 완성시킨다.
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


def find_prime(n: int) -> list[int]:
    '''
    n의 소인수분해를 수행하는 코드
    https://namu.wiki/w/%EC%86%8C%EC%9D%B8%EC%88%98%EB%B6%84%ED%95%B4/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
    '''
    if n <= 2:
        return [n, ]
    for idx in range(2, n):
        if n % idx == 0:
            ret_list = []
            val_a = find_prime(idx)
            val_b = find_prime(n // idx)
            ret_list = val_a + val_b
            return ret_list
    return [n, ]


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
    print(-1 if result is None or len(result)
          == 1 else ' '.join(map(str, result)))


# end main
