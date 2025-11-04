# Input
# cacheSize = 캐시 크기  (0~30)
# cities = 도시이름 배열 (최대 100,000)
# 도시 이름 = 공백, 숫자, 특수문자가 없는 영문자, 대소문자 구분 X, 최대 20자
# Output
# 입력된 도시 이름을 배열 순서대로 처리 시 총 실행시간
# LRU: Least Recently Used
# deque!!!!

from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)  # keyPoint
    # O(N)
    for c in cities:
        c = c.lower()
        if c in cache:
            cache.remove(c)
            cache.append(c)  # 맨 뒤로
            answer += 1
        else:
            answer += 5
            cache.append(c)  # left 원소 자동 delete

    return answer
