# Input
# new_id = 신규 유저 입력 아이디 (1~1000)
# Output
# 7단계 처리 과정 후 추천 아이디
# 1. new_id 모든 대문자를 소문자
# 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
# 3. .가 2번 이상 연속 -> .로 치환
# 4. .가 처음이나 끝이면 제거
# 5. 빈 문자열 -> "a"
# 6. len(16) 이상이면 초반 15자만, 제거 후 .가 끝에 있으면 제거
# 7. len(2) 이하면 마지막 문자를 3이 될때까지 반복
# Hint
# 정규 표현식, 문자열

import re


def solution(new_id):
    answer = ''

    pattern = r"[a-z0-9-_.]*"  # For Rule 2
    pattern2 = r"\.{2,}"  # For Rule 3

    answer = re.sub(pattern2, ".", "".join(re.findall(
        pattern, new_id.lower()))).strip(".")  # Rule1 ~ Rule 4
    if not answer:
        answer += "a"  # Rule 5
    if len(answer) >= 16:
        answer = answer[:15].strip(".")
    while len(answer) <= 2:
        answer += answer[-1]

    return answer
