# Input
# fees = 주차 요금 (길이 4) = 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
# records = 자동차의 입/출차 내역 문자열 배열, "시각 차량번호 내역"
# 시각 = "HH:MM" = 입차 및 출차된 시각
# 차량 번호 = '0~9' 로 구성된 길이 4 문자열
# 내역 =  In or OUT
# Output
# 차량 번호가 작은 자동차부터 청구할 주차 요금
# Hint
# stack

from collections import deque
import math


def solution(fees, records):
    answer = {}
    count = {}

    for record in records:
        time, num, _ = record.split()
        answer[num] = 0
        time_minutes = int(time.split(":")[0])*60 + int(time.split(":")[1])
        if num in count:
            count[num].append(time_minutes)
        else:
            count[num] = deque([time_minutes])

    for c in count:
        time = 0
        while count[c]:
            start = count[c].popleft()
            end = count[c].popleft() if count[c] else 23 * 60 + 59
            time += end - start

        if time <= fees[0]:
            answer[c] = fees[1]
        else:
            answer[c] = fees[1] + math.ceil((time-fees[0]) / fees[2]) * fees[3]

    answer = sorted(answer.items(), key=lambda item: item[0])
    answer = [x[1] for x in answer]
    return answer
