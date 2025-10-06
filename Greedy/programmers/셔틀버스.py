# Input
# n = 셔틀 운행 횟수 (0~10)
# t = 셔틀 운행 간격 (0~60)
# m = 한 셔틀에 탈 수 있는 최대 크루 수 (0~45)
# timetable = 크루가 대기열에 도착하는 시각을 모은 array, "HH:MM" 형태
# 도착한 순간에 선 크루까지 포함!
# Output
# 콘이 사무실로 갈 수 있는 제일 늦은 도착 시각
# 같은 시각인 경우 제일 뒤에 선다.
# 어떤 크루도 다음날 셔틀을 타는 일은 없다
# Hint
# Greedy
# 어떤 자료구조? = dict

def solution(n, t, m, timetable):
    time = dict()
    start = 60 * 9  # 분으로 바꾸기
    # 버스 시간표:인원 수
    for i in range(n):
        time[start] = []
        start += t

    timetable.sort()  # 먼저 정렬해야 함!!!
    for mem in timetable:
        mem_h, mem_m = int(mem[:2]), int(mem[3:])
        mem_time = mem_h*60 + mem_m  # 크루의 시간
        for t in time:
            if len(time[t]) == m:  # 인원 수 꽉 참
                continue  # 다음 시간으로
            if mem_time <= t:  # 가능한 시간대라면
                time[t].append(mem_time)
                break

    # 콘의 시간
    answer = 0
    last_time, last = time.popitem()
    last.sort()

    if len(last) != m:
        answer = last_time
    else:  # len(last) == m, 마지막 탑승자보다 일찍 오면 된다.
        if last[0] == last[-1]:  # 같으면
            answer = last[0]-1
        else:
            answer = last[-1]-1

    return f"{answer//60:02}:{answer%60:02}"
