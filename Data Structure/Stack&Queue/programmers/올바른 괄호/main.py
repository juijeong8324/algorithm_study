# Input
# s = '(' 또는 ')'로 이루어진 문자열
# Output
# 올바른 괄호면 true
# Hint
# 딱 봐도 Stack
# "(" = stack append
# ")" = stack pop

def solution(s):
    answer = True
    stack = []

    for c in s:
        if c == '(':
            stack.append("(")
        else:  # ')' 일 때
            if not stack:  # empty
                return False
            else:
                stack.pop()

    if stack:  # 비어 있지 않으면
        return False

    return True
