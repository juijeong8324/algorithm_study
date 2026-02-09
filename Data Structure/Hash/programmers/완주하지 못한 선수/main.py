
# Input
# participant = 마라톤에 참여한 선수들의 이름이 담긴 배열 (1~100,000)
# # 동명이인 존재 가능
# completion = 완주한 선수들의 이름이 담김 배열 (len(participant)-1)
# Output
# 완주 못한 선수의 이름을 출력 (한 명만 존재)
# Hint
# Hash = 빠른 search가 필요함!! Time complexity = O(1)
# dict = 참가자 이름을 key로 하여 빈도수를 저장

from collections import defaultdict


def solution(participant, completion):
    hash_table = defaultdict(int)

    for p in participant:  # 참가자 명단 정리
        hash_table[p] += 1

    for c in completion:  # 완주 선수 정리
        hash_table[c] -= 1

    for key, value in hash_table.items():
        if value > 0:  # 완주 못한 선수
            return key
