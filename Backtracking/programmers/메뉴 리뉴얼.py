# Input
# orders = 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 (2~20)
#        = elements 2 ~ 10 문자열
#        = 알파벳 대문자
# course = 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열
#        = 2 ~ 10 자연수 오름차순
# Output
# 코스 요리 메뉴 -> 최소 2가지 이상 단품 메뉴, 최소 2명 이상, 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴
# 새로 추가하게 될 코스요리의 메뉴 구성 문자열, 오름차순
# Hint
# Dict, backtracking
# Time Complexity
# 20 * 10 * (10C2~10C10)
new_course = {}


def find_comb(data, k):  # 주어진 문자열, 선택할 코스 개수
    def backtrack(start, curr):  # 시작 index, 현재 문자열
        if len(curr) == k:
            if curr in new_course:
                new_course[curr] += 1
            else:
                new_course[curr] = 1
            return

        for s in range(start, len(data)):
            curr += data[s]
            backtrack(s+1, curr)
            curr = curr[:-1]  # 제거

    backtrack(0, "")
    return


def solution(orders, course):
    answer = []

    # 모든 조합 찾기
    for order in orders:
        order = "".join(sorted(order))
        for c in course:
            find_comb(order, c)

    data_set = {}
    for n_c in new_course:
        n = len(n_c)
        val = new_course[n_c]
        if val < 2:
            continue

        if n not in data_set:
            data_set[n] = (val, [n_c])  # 빈도수. 목록
        else:
            max_val, current_list = data_set[n]
            if val > max_val:  # update
                data_set[n] = (val, [n_c])
            elif val == max_val:
                current_list.append(n_c)

    for d in data_set:
        answer += data_set[d][1]

    answer.sort()

    return answer
