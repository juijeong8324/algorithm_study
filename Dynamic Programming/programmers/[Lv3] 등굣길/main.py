# Input
# m x n = 격자의 크기 (1이상 100 이하)
# puddles = 물이 잠긴 지역의 좌표를 담은 2차원 배열
# 물이 잠긴 지역 0개 이상 10개 이하
# Output
# (1,1) 에서 (m,n)까지
# 오른쪽과 아래쪽만으로만 움직여 집에서 학교까지 갈 수 있는 최단경로 개수
# 이를 1,000,000,007로만 나눈 나머지
# Hint
# 이미 오른쪽과 아래쪽으로만 이동하므로 모든 경로가 최단 경로임
# DP[i][j] = (i, j)까지 도달할 수 있는 경로 개수

def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]

    # 초기값
    dp[1][1] = 1

    # 물덩이 처리
    for i, j in puddles:
        dp[j][i] = -1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1:
                continue  # (1,1) 처리
            if dp[i][j] == -1:
                dp[i][j] = 0  # 물덩이는 따로 처리
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    return dp[n][m] % 1000000007
