# Input
# scoville = 음식의 스코빌 지수 담은 배열 (길이: 2~1,000,000)
# K = 원하는 스코빌 지수 (길이: 0~1,000,000,00)
# Output
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수
# 스코빌 지수가 가장 낮은 두 개의 음식
# 섞은 음식 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while scoville:
        if scoville[0] >= K:  # 가장 최소가 K 이상이면 종료
            break

        if len(scoville) < 2:  # K 미만인데, 더 이상 만들 수 없을 떄
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        heapq.heappush(scoville, first + (second*2))
        answer += 1

    return answer
