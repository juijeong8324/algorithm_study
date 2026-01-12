# Input
# answers = 시험 문제 정답 (최대 10000개)
# 문제 정답은 1,2,3,4,5 중 하나
# Output
# 가장 많은 문제를 맞힌 사람을 배열에 담아 return
# Hint
# Brute Force
# 걍 정답을 수포자 한 명씩 하나씩 비교해봐야 하니까

def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]  # 5개
    two = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10개

    count_1 = 0
    count_2 = 0
    count_3 = 0

    for idx, p in enumerate(answers):
        count_1 += int(one[idx % 5] == p)
        count_2 += int(two[idx % 8] == p)
        count_3 += int(thr[idx % 10] == p)

    m = max(count_1, count_2, count_3)
    print(m)
    if(count_1 == m):
        answer.append(1)
    if(count_2 == m):
        answer.append(2)
    if(count_3 == m):
        answer.append(3)

    return answer
