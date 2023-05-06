'''
# src
boj.kr/11066

# category
dp

# verdict
[다음 링크](https://www.acmicpc.net/board/view/115640)에 따르면, O(N ** 3) 시간복잡도로 구현된
재귀 파이썬 코드가 시간초과가 난다는 말이 있다. 지금 내가 쓴 코드의 시간복잡도는 세제곱인지조차 잘 모르겠다.
일단 비재귀로 바꾼 다음 재시도 해보자.
'''
import sys
input = sys.stdin.readline

INTMAX = 99_999


def sum_between(sum, i, j):
    if i == 0:
        return sum[j]
    return sum[j] - sum[i-1]


def solution(k: list[int]) -> int:
    '''
    non-recursive dynamic programming
    '''
    K = len(k)
    dp = [[0 for _ in range(K)] for _ in range(K)]
    my_sum = [k[0]]
    for i in range(1, K):
        my_sum.append(my_sum[i-1] + k[i])

    # length = 0인 모든 dp[i][i]에 대하여 k[i] = 0이다.

    length = 1
    for left in range(0, K - length):
        # length = 1인 모든 dp[i][i + length]에 대하여 k[i] + k[i + len]이다
        right = left + length
        dp[left][right] = k[left] + k[right]

    for length in range(2, K + 1):
        # length >= 2 인 모든 dp[i][j]에 대하여 다음 식을 만족한다.
        # dp[i][j] = sum[i:j] + min(
        #    for l in range(i, j):
        #        dp[i][l] + dp[l+1][j]
        # )
        for left in range(0, K - length):
            right = left + length

            best = INTMAX
            for mid in range(left, right):
                best = min(best, dp[left][mid] + dp[mid + 1][right])

            dp[left][right] = sum_between(my_sum, left, right) + best

    return dp[0][K-1]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        K = int(input())
        k = [int(x) for x in input().split()]
        print(solution(k))
# end main
