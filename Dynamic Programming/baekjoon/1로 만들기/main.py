# Input
# N = 정수
# Output
# N에서 1로 만들기 위한 연산을 사용하는 횟수의 최솟값
# Hint
# DP = N의 연산 최솟값은 N/3, N/2, N-1 중에서 연산 최솟값 + 1

import sys
input = sys.stdin.readline

N = int(input().strip())
dp = [0 for _ in range(N+1)]

dp[1] = 0
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[N])
