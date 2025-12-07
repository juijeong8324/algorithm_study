# Input
# n = 진법 (2 ~ 16)
# t = 미리 구할 숫자의 갯수 (0 ~ 1000)
# m = 게임에 참가하는 인원 (2 ~ 100)
# p = 튜브의 순서 (1 <= p <= m)
# Output
# 튜브가 말해야 하는 숫자 t개를 공백 없이 차례대로 나타낸 문자열 (10~15 -> A~F)
# 10 이상의 숫자는 한 자리씩 끊어서 Ex) 21 = 2, 1
# 단 10~15 는 A~F로
# Hint
# 구현 + 수학 인듯?

def solution(n, t, m, p):
    answer = "0"
    digit = "0123456789ABCDEF"

    for num in range(1, m*t):
        result = ""
        # num을 n진수로 변환
        while num > 0:
            remainder = num % n
            num = num // n
            result += digit[remainder]
        answer += result[::-1]

    return answer[p-1::m][:t]  # answer의 p-1번 부터 +m으로 list 반환 -> t번째 요소까지
