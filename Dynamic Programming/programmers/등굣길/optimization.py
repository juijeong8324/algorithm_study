# dp[i]: 현재 행에서 i번째 열까지의 경로 수
# 위쪽 값은 이전 행에서 오는 값임을 이용!!
def solution(m, n, puddles):
    puddle_set = {(j, i) for j, i in puddles}

    dp = [0] * (m + 1)
    dp[1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (j, i) in puddle_set:
                dp[j] = 0
            elif not (i == j == 1):
                dp[j] = (dp[j] + dp[j - 1]) % 1000000007  # 위쪽 + 오른쪽

    return dp[m] % 1000000007
