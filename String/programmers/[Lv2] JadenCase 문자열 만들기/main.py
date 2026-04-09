# Input
# 문자열 s (1 이상 200 이하)
# Output
# JadenCase로 바꾼 문자열을 return
# 모든 단어의 첫 문자가 대문자이고 그 외의 알파벳은 소문자인 문자열
# 단, 첫 문자가 알파벳이 아닐 때 이어지는 알파벳은 소문자
# Hint
# 구현임

def solution(s):
    answer = []

    words = s.split(' ')
    for word in words:
        # String is Immutable in Python
        word = word[:1].upper() + word[1:].lower()
        # Use slicing to avoid IndexError on empty strings, but not indexing

        answer.append(word)

    return ' '.join(answer)
