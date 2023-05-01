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


def sol(W, N, M) -> int:
    DP = [[0 for _ in range(M)] for _ in range(N)]

    DP[0][0] = W[A[0]][B[0]]
    for j in range(1, M):
        # init
        DP[0][j] = max(DP[0][j-1], W[A[0]][B[j]])

    for i in range(0, N):
        for j in range(1, M):
            # A 학교의 i와 B 학교의 j 이하의 번호를 가진 학생이 악수를 나눌 때
            # 얻을 수 있는 최대 만족도를 리턴하세요
            case1 = W[A[i]][B[j]] + \
                (DP[i - 1][j - 1] if i > 0 else 0)  # i,j has hand-shaked
            case2 = DP[i][j - 1]  # i has already hand-shaked
            case3 = DP[i - 1][j] \
                if i > 0 else 0  # i never want to hand-shake
            DP[i][j] = max(max(case1, case2), case3)

    return DP[N - 1][M - 1]


submit = sol(W, N, M)
print(submit)
