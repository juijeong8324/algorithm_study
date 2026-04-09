# Input
# today = 오늘 날짜, "YYYY.MM.DD"
# terms = 약관의 유효기간 1차원 문자열 배열, 1~20, "[A-Z] [1-100]달"
# privacies = 수집된 개인정보의 정보 1차원 문자열 배열, 1~100, "YYYY.MM.DD [A-Z]"
# Output
# 파기해야 할 개인정보의 번호, 오름차순, 1차원 정수 배열
# 2021.01.05 -> +12달 -1일 -> 2022.01.04 (보관 가능 날짜)
# Hint
# 문자열, 구현
def solution(today, terms, privacies):
    answer = []
    terms_dict = {}

    # 오늘 날짜
    Y, M, D = map(int, today.split("."))
    today_num = Y * 12 * 28 + M * 28 + D

    # 약관 정보
    for t in terms:
        a, b = t.split()  # 약관 종류, 달
        terms_dict[a] = int(b)

    # O(N)
    for idx, p in enumerate(privacies):
        day, c = p.split()
        y, m, d = map(int, day.split("."))
        p_num = y * 12 * 28 + m * 28 + d
        p_num += terms_dict[c] * 28
        if p_num <= today_num:
            answer.append(idx+1)

    return answer
