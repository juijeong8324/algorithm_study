# Input
# users = 사용자 n명의 구매 기준 담은 2차원 정수 배열 = [비율, 가격] = {비율}% 할인 이모티콘 구매, 가격 이상
# emoticons = 이모티콘 m개의 정가를 담은 1차원 정수 배열 (1~7)
# Output
# 행사 목적 최대 달성 시 서비스 가입 수와 이모티콘 매출액
# 행사 목적 = 서비스 가입자 최대 > 판매액 최대
# 행사 방식 = 1. n명에게 이모티콘 m개 할인 판매
#           2. 할인율 0.1, 0.2, 0.3, 0.4
# 사용자 = 1. 각 사용자들은 일정 비율 이상 할인 이모티콘 구매
# 2. 이모티콘 구매 비용 합이 일정 가격 이상 시, 구매 취소 후 가입
# Hint
# DFS = 모든 각 이모티콘의 할인율 경우의 수
# Brute Force
# Time Complexity = 4^7 * 100 * 7 < 1억 미만

from itertools import product  # 중복 순열


def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)
    answer = [0, 0]
    # [10, 20, 30, 40] 중에 중복 허용으로 m개 선택
    sales = list(product([10, 20, 30, 40], repeat=m))
    for s in sales:
        service = 0
        bill = 0
        for user in users:
            ratio, b = user[0], user[1]
            total = 0  # 총액
            for idx, e in enumerate(emoticons):
                if s[idx] < ratio:
                    continue
                total += e*(100 - s[idx]) // 100
            if total >= b:  # 서비스 가입자
                service += 1
            else:  # 혹은 모두 구매
                bill += total
        # 결과
        if answer[0] < service:
            answer[0] = service
            answer[1] = bill
        elif answer[0] == service:
            answer[1] = max(answer[1], bill)

    return answer

# itertools 안 쓸 때


def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)
    sales = []
    answer = [0, 0]

    def dfs(level):  # 선택한 이모티콘 개수, list
        if level == m:  # 모두 선택 시 계산
            service = 0  # 가입자 수
            bill = 0  # 이모티콘 매출액
            for user in users:
                ratio, b = user[0], user[1]
                total = 0  # 총액
                for idx, e in enumerate(emoticons):
                    if sales[idx] < ratio:
                        continue
                    total += e*(100 - sales[idx]) // 100
                if total >= b:  # 서비스 가입자
                    service += 1
                else:  # 혹은 모두 구매
                    bill += total

            # 계산
            if answer[0] < service:
                answer[0] = service
                answer[1] = bill
            elif answer[0] == service and answer[1] < bill:
                answer[1] = bill
            return  # 종료

        for i in range(40, 0, -10):  # 현재 level에서 4개 선택
            sales.append(i)
            dfs(level+1)
            sales.pop()  # 백트래킹

    dfs(0)
    return answer
