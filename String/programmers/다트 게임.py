# Input
# "점수|보너스|옵션" (점수=0~10, 보너스=SDT, 옵셥=*#X) 의 3세트
# SDT = 점수**1, 점수**2, 점수**3
# * = 해당 점수 바로 전에 얻은 점수 각 2배로, 첫 번재면 첫 번쨰만
# # = 해당 점수 마이너스
# Output
# 3번의 기회에서 얻은 점수 합계
# 정규 표현식

import re


def solution(dartResult):
    score = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}

    c = re.compile('(\d+)([SDT])([*#]?)')  # 정규표현식 object
    problem = c.findall(dartResult)
    for idx, dart in enumerate(problem):
        s, b, o = dart
        score.append(int(s)**bonus[b] * option[o])
        if idx > 0 and o == '*':
            score[idx-1] *= 2

    return sum(score)
