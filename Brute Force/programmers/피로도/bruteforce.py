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
# 던전 개수가 작기 때문에 Brtue Force로 모든 경로를 탐색
# itertools 사용
# DFS로 구현하는 경우, 모든 던전 방문 후 마지막에
# 답 return

from itertools import permutations


def solution(k, dungeons):
    answer = 0
    N = len(dungeons)

    for p in permutations(range(N)):  # 각 경우의 수에 대해서
        currK = k
        currA = 0

        for idx in p:
            if dungeons[idx][0] <= currK:  # 방문 가능하다면
                currK -= dungeons[idx][1]
                currA += 1

        answer = max(answer, currA)
    return answer
