# Input
# survey = 질문마다 판단 지표 담은 1차원 문자열 배열 (1~1000)
# surver[i][0] = 비동의 선택지 점수 받는 선택지, surver[i][1] = 동의 선택지 점수 받는 선택지
# choices = 각 질문마다 선택한 선택지 담은 1차원 정수 배열 (1~1000)
# choices[i] = 검사자가 선택한 i+1번째 질문의 선택지
# Output
# 검사자의 성격 유형 검사 결과를 지표 번호 순서대로 return
# 성격 유형 검사
# 총 16가지
# n개의 질문에 7개의 선택지
# 각 지표에서 각 성격 유형 점수가 같으면, 두 성격 유형 중 사전 순으로!

from collections import defaultdict


def solution(survey, choices):
    answer = ''
    mbti = defaultdict(int)
    types = ['RT', 'CF', 'JM', 'AN']

    # Survey
    for personality, choice in zip(survey, choices):
        if choice > 4:
            mbti[personality[1]] += choice - 4
        elif choice < 4:
            mbti[personality[0]] += 4 - choice

    # complete MBTI
    for t in types:
        if mbti[t[0]] >= mbti[t[1]]:
            answer += t[0]
        else:
            answer += t[1]

    return answer
