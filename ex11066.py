'''
[src]
boj.kr/11066

[category]
dp
'''
import sys
input = sys.stdin.readline

INTMAX = 99_999
dp = []


def sum_between(sum, i, j):
    if i == 0:
        return sum[j]
    return sum[j] - sum[i-1]


def solution_recur(k, _sum, i, j) -> int:
    '''
    [base case]
    ```python
    dp[i][i] = 0
    dp[i][i + 1] = k[i] + k[i+1]
    ```python

    [general case]
    ```python
    dp[i][j] = sum[i : j] + min(for l in range(i, j):
                                    dp[i][l] + dp[l + 1][j])
    ```python
    '''
    global dp
    if (dp[i][j] != 0):
        return dp[i][j]

    if (i == j):
        return 0
    if (i + 1 == j):
        dp[i][j] = k[i] + k[j]
        return dp[i][j]

    best = INTMAX
    for left in range(i, j):
        best = min(best, solution_recur(k, _sum, i, left) +
                   solution_recur(k, _sum, left+1, j))

    dp[i][j] = sum_between(_sum, i, j) + best
    return dp[i][j]


def solution(k) -> int:
    global dp

    K = len(k)
    dp = [[0 for _ in range(K)] for _ in range(K)]

    _sum = [k[0]]
    for i in range(1, len(k)):
        _sum.append(_sum[i - 1] + k[i])
    return solution_recur(k, _sum, 0, len(k) - 1)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        K = int(input())
        k = [int(x) for x in input().split()]
        print(solution(k))
# end main
