'''
boj.kr/27212
'''
import sys


def sol(
        W: list[list[int]],
        A: list[int],
        B: list[int]
) -> int:

    N = len(A)
    M = len(B)

    dp = [[0 for _ in range(M)] for _ in range(N)]

    # init base case
    dp[0][0] = W[A[0] - 1][B[0] - 1]
    for j in range(1, M):
        dp[0][j] = max(dp[0][j - 1], W[A[0] - 1][B[j] - 1])
    dp[1][0] = max(dp[0][0], W[A[1] - 1][B[0] - 1])

    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = dp[i-1][j-1] + W[A[i] - 1][B[j] - 1]
            dp[i][j] = max(dp[i][j], dp[i][j - 1])
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

    return dp[N-1][M-1]


if __name__ == '__main__':

    # input
    [N, M, C] = [int(s) for s in sys.stdin.readline().split(' ')]

    W = [list(map(int, sys.stdin.readline().split())) for _ in range(C)]

    A = [int(s) for s in sys.stdin.readline().split(' ')]
    B = [int(s) for s in sys.stdin.readline().split(' ')]

    # solve
    submit = sol(W, A, B)
    print(submit)
