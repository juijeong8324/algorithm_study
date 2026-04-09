# Input
# n = 퇴근까지 남은 시간 (1,000,000 이하 자연수)
# works = 각 일에 대한 작업량 (len = 1 이상 20,000 이하) (원소는 50000 이하)
# Output
# 야근 피로도 최소화한 값
# 퇴근까지 남은 시간에 대해 작업량을 처리 이때, 1시간 동안 작업량 1만큼 처리
# 야근 피로도 = 각 남은 일의 작업량**2 합
# Hint
# Greedy = 큰 작업량 부터 먼저 처리, 제곱 합이 최소가 되려면 큰 수를 먼저 줄여야 하기 때문
# Time Complextiy = O(n) * O(log m) -> heapq로 최댓값 찾기 = O(nlogm)

import heapq


def solution(n, works):
    heap = [-w for w in works]  # 최대합으로 처리하기 위함
    heapq.heapify(heap)

    for _ in range(n):  # 작업량 동안 반복
        max_work = - heapq.heappop(heap)
        if max_work == 0:
            break
        max_work -= 1
        heapq.heappush(heap, -max_work)

    answer = sum(w*w for w in heap)

    return answer
