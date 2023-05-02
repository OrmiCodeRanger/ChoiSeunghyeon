'''
boj.kr/27212
'''
import sys

UNDEFINED = -1

[N, M, C] = [int(s) for s in sys.stdin.readline().split(' ')]

W = []

for row in range(C):
    row_list = [int(s) for s in sys.stdin.readline().split(' ')]
    W.append(row_list)

# 인덱스가 1부터 시작하기 때문에 1 빼줌
A = [int(s) - 1 for s in sys.stdin.readline().split(' ')]
B = [int(s) - 1 for s in sys.stdin.readline().split(' ')]

DP = [[UNDEFINED for _ in range(M)] for _ in range(N)]


def sol(W, N, M, A, B) -> int:

    dp = [[0 for _ in range(M)] for _ in range(N)]

    # init base case
    dp[0][0] = W[A[0]][B[0]]
    for j in range(1, M):
        dp[0][j] = max(dp[0][j - 1], W[A[0]][B[j]])
    dp[1][0] = max(dp[0][0], W[A[1]][B[0]])

    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = dp[i-1][j-1] + W[A[i]][B[j]]
            dp[i][j] = max(dp[i][j], dp[i][j - 1])
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

    return dp[N-1][M-1]


submit = sol(W, N, M, A, B)
print(submit)
