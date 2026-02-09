# Input
# n = 전체 학생 수 (2~30)
# lost = 체육복 도난당한 학생 번호 담긴 배열 (1~n, 중복 없음)
# reserve = 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 (1~n, 중복 없음)
# Output
# 체육 수업을 들을 수 있는 학생의 최댓값
# 바로 앞뒤 번호 학생에게만 빌려줄 수 있음! 
# 여벌 체육복이 있는 학생만 빌릴 수 있음
# 여벌 체육복이 있는 학생이 도난당하면 빌려줄 수 없음 
# Hint
# Greedy = 여분 옷 있는 친구의 앞 or 뒤에 나눠주기 (단 1번만 가능)

def solution(n, lost, reserve):
    # lost와 reserve가 오름차순이라는 보장 없음 
    # 여분의 옷이 있는 친구가 도난 당한 경우 확인
    r = set(reserve) - set(lost)
    l = set(lost) - set(reserve)
    
    # 정렬 
    r = sorted(r)
    
    # 여분 옷 있는 친구 기준으로 
    for s in r:
        if s-1 in l:
            l.remove(s-1)
        elif s+1 in l:
            l.remove(s+1)

    return n - len(l)