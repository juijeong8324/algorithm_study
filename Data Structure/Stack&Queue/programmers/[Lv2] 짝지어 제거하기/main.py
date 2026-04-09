# Input
# S = 문자열 
# # 모두 소문자
# # 길이는 1,000,000 이하의 자연수 
# Output
# 짝지어 제거하기 성공 시 1 아니면 0
# 짝지어 제거하기 
# # 알파벳 소문자로 이루어진 문자열 
# # 같은 알파벳 2개가 붙어있는 짝 -> 둘을 제거 -> 앞 뒤로 문자열을 이어붙이기! -> 모두 제거될 때까지
# Hint
# Naive = 문자열을 순회하면서 제거하는 순간 처음부터 다시 순회
# 하지만 s = s[:i] + s[i+2:]의 경우 매 제거마다 문자열 전체를 복사... → O(N^2)의 시간복잡도! 
# # Stack = 순회하면서 stack top과 현재 문자가 같으면 pop, 다르면 push
# → 중간에 새로 생기는 짝도 자연스럽게 처리됨 
# → O(N)의 시간복잡도! 

def solution(s):
    stack = []
    
    stack.append(s[0])
    for i in range(1, len(s)):
        if not len(stack) or stack[-1] != s[i]:
            stack.append(s[i])
        else:
            stack.pop()
            
    return int(not(stack))