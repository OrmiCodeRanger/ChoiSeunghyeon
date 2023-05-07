"""Dearrangement(완전순열)
boj.kr/1947

자신의 선물은 자기가 받을 수 없을 때 N명의 사람들이 선물을 나누어 갖는 경우의 수

Case 1) A1이 선물 a2를, A2가 선물 a1를 상호교환하였을 경우,
    남은 선물 {a3, a4, ... , an}이 다시 완전순열을 이룸.

Case 2) A1이 선물 a2를 받았지만 A2가 선물 a1을 받지 못한 경우,
    A2 자리에 a1이 오지 못하기 때문에 A2가 A1에 빙의하면 남은 선물
    {a1, a3, a4, ... , an}이 다시 완전순열을 이룸.

Case 1 + Case2) 두 경우의 수는 완전히 독립적이므로 합연산을 수행하면 된다.
    그리고 각 케이스 마다 어울릴 수 있는 쌍이 (n-1)가지 이므로 점화식은
    D(n) = (n-1)(D(n-2) + D(n-1))
"""

MOD_BY = 1_000_000_000

if __name__ == "__main__":
    n = int(input())
    dp = [0 for _ in range(n+1)]

    dp[0] = 1
    dp[1] = 0

    for i in range(2, n + 1):
        dp[i] = ((i - 1) * (dp[i - 2] + dp[i - 1])) % MOD_BY

    print(dp[n])

# end main
