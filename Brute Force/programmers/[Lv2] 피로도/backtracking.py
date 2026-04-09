# Input
# k = 현재 피로도 (1~5,000)
# dungeons = 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열
# # n = 던전 개수 (1~8)
# # m = ["최소 필요 피로도", "소모 피로도"] 모두 1이상 1,000 이하
# # 최소 필요 피로도는 소모 피로도보다 크거나 같다.
# Output
# 유저가 탐험할 수 있는 최대 던전 수
# 각 던전마다 -> 탐험 시작 전 필요한 최소 필요 피로도를 맞추기, 탐험 후 소모 피로도 만큼 소모
# Hint
# 모든 던전에 대해서 방문한 후 던전 수 계산할 필요 X
# 최소 필요 피로도를 만족하지 못하는 던전은 cut -> Backtracking

def solution(k, dungeons):
    answer = 0
    N = len(dungeons)
    vis = [0]*N

    def dfs(curr, count):  # 현재 피도로, 방문 가능한 던전
        nonlocal answer  # local variable 방지
        answer = max(answer, count)

        for i in range(N):
            # 방문 X 던전 중 최소 필요도 만족하는 경우데 대해서만(Pruning)
            if not vis[i] and dungeons[i][0] <= curr:
                # 방문(재귀)
                vis[i] = 1
                dfs(curr-dungeons[i][1], count+1)
                # Backtrack
                vis[i] = 0

    dfs(k, 0)
    return answer
