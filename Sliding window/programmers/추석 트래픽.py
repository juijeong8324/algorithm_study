# Input
# lines = log 문자열(1~2000), "S(요청 응답 완료 시간) T(처리시간)", S 기준으로 오름차순
# S = hh:mm:ss.sss
# T = s (소숫점 셋째 자리), 시작시간 + 끝시간, 0.001~3.000
# Timeout = 3초
# Output
# lines 배열에 대한 초당 최대 처리량

def solution(lines):
    times = []
    n = len(lines)

    for line in lines:
        _, S, T = line.split()  # 공백을 기준으로 분리
        h, m, s = S.split(":")  # hh, mm, s로 분리
        end_s = float(h)*3600 + float(m)*60 + float(s)  # 초 단위로 변환
        start_s = end_s - float(T[:-1]) + 0.001  # 시작도 포함
        # 소수점 제거 후 log에 추가
        times.append((start_s, end_s))

    check_points = set()  # 모든 구간 시작점 저장
    for start_s, end_s in times:
        check_points.add(end_s)  # 트래픽 끝점도 시작이 될 수 있음
        check_points.add(start_s)

    max_throughput = 0
    for point in check_points:
        start_of_interval = point
        end_of_interval = point + 1.000  # 제외

        count = 0
        for start_j, end_j in times:  # 각 트래픽이 구간에 포함되는가?
            if start_of_interval < end_j + 0.001 and end_of_interval > start_j:
                count += 1

        max_throughput = max(max_throughput, count)

    return max_throughput
