# Input
# people = 사람들 몸무게 담은 배열 (size=1~50000, each elem = 40~240)
# limit = 구명보트 무게 제한 (40~240)
# Output
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값
# 구명보트는 한 번에 최대 2명씩
# 사람들을 구출할 수 없는 경우는 없다.
# Hint
# Greedy = 최대한 2명씩 태워야 함 = 큰 사람 + 작은 사람 or 큰 사람 조합만 존재
# Two pointer = 현재 가능한 최댓값과 최솟값의 조합으로 태우는게 best
# 만약 인원 제한이 없다면? = 난이도 올라감. DP..

def solution(people, limit):
    answer = 0
    people.sort()

    low = 0
    high = len(people)-1

    while low <= high:
        if people[low] + people[high] <= limit:
            answer += 1
            low += 1
            high -= 1
        else:
            answer += 1
            high -= 1

    return answer
