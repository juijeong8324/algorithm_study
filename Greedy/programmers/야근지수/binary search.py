# Input
# n = 퇴근까지 남은 시간 (1,000,000 이하 자연수)
# works = 각 일에 대한 작업량 (len = 1 이상 20,000 이하) (원소는 50000 이하)
# Output
# 야근 피로도 최소화한 값
# 1시간 동안 작업량 1만큼 처리
# 야근 피로도 = 각 남은 일의 작업량**2 합
# Hint
# Greedy = 큰 작업량 부터 먼저 처리 하되
# 이분탐색 = baseline 작업량을 찾기 (baseline에서 남은 시간을 계산해서 조정)
# baseline을 정한 후 마지막에 Greedy로 남은 작업량 처리 (모두 baseline과 같은 필요 없음)
# Time Compelxity = O(mlogm) sort에서 지배적임

def solution(n, works):
    if n >= sum(works):
        return 0

    works.sort(reverse=True)
    low, high = 0, works[0]

    # n < sum(works) 에 대해서
    while low < high:
        mid = (low + high) // 2

        # mid 이상의 모든 작업을 mid로 줄이기
        # 이떄 큰 수 부터 먼저 줄이고
        # 음수인 경우 제외
        time_needed = sum(max(0, w - mid) for w in works)

        if time_needed <= n:  # 작업한 량이 너무 적은 경우
            high = mid
        else:
            low = mid + 1

    answer = 0
    remaining_time = n - sum(max(0, w - low) for w in works)

    # 최종 남은 작업량 결정
    for i, w in enumerate(works):
        reduced = max(0, w - low)  # 기존 작업한 량
        if i < remaining_time:  # baseline에서 추가 제거
            reduced += 1  # 업데이트된 작업한 량
        answer += (w - reduced) ** 2  # w - 작업한 량

    return answer
