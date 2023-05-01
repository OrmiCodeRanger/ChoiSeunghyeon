'''
boj.kr/27212
'''
import sys
sys.setrecursionlimit(10 ** 9)

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


def sol_recur(i: int, j: int) -> int:
    '''
    i와 j가 손을 잡았을 때, 전체 인원의 가장 높은 만족도를 리턴하세요.
    '''

    global DP, W, N, M, C

    # end condition
    if DP[i][j] != UNDEFINED:
        return DP[i][j]
    # end condition
    if i == N-1 and j == M-1:
        DP[i][j] = W[A[i]][B[j]]
        return DP[i][j]

    best = 0
    for next_i in range(i + 1, N):
        for next_j in range(j + 1, M):
            result = sol_recur(next_i, next_j)
            if best < result:
                best = result

    DP[i][j] = best + W[A[i]][B[j]]

    return DP[i][j]


submit = 0
for i in range(N):
    for j in range(M):
        submit = max(submit,  sol_recur(i, j))
print(submit)
