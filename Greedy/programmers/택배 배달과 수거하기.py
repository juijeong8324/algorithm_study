# Input
# cap = 트럭에 실을 수 있는 재활용 택배 상자의 최대 개수, (1~50)
# n = 배달할 집의 개수 (1~100000)
# deliveries = 각 집에 배달할 재활용 택배 상자의 개수를 담은 1차원 정수 배열, 길이 n (0~50)
# pickups = 각 집에서 수거할 빈 재활용 택배 상자의 개수를 담은 1차원 정수 배열, 길이 n (0~50)
# Output
# 트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리
# Hint
# greedy = 최대한 cap 개수를 채워서 이동

def solution(cap, n, deliveries, pickups):
    answer, d, p = 0, 0, 0

    for i in range(n-1, -1, -1):
        # d와 p는 현재 위치 i에 대해 아직 처리해야 할 총 물량
        d += deliveries[i]
        p += pickups[i]

        cnt = 0  # 현재 위치 i를 몇 번 반복?
        # 물량이 없거나 (d=0 or p=0) 다음 집(i-1) 용량까지 처리 가능한 경우(d<0 or p<0)
        while d > 0 or p > 0:
            cnt += 1
            d -= cap
            p -= cap

        # d < 0 또는 p < 0 라면, 현재까지의 거리의 배달 및 수거가 다음 집(i-1)의 물량 처리에도 활용될 수 있다는 의미

        answer += ((i+1)*2*cnt)  # 현재 i+1 왕복을 얼마나?

    return answer
