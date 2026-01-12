# Input
# s = 일부 자릿수가 영단어로 바뀌거나 그대로인 문자열
# Output
# s가 의미하는 원래 숫자를 return
# EX)
# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"

num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
