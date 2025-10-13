# Input
# n = 양의 정수 (1~1000000)
# k = k진수 (3~10)
# Output
# n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 조건에 맞는 소수 개수
# 단, 소수는 10진법 기준에서 소수
# 1. 소수 양쪽에 0이 있는 경우 0P0
# 2. 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우 P0
# 3. 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우 0P
# 4. 아무것도 없는 P
# 5. P는 각 자릿수에 0을 포함하지 않음. EX) 101 은 P가 아님
# Hint
# 문자열, Math

import re
import math


def convert(n, k):
    if n == 1:
        return "1"

    digit = []
    while n != 0:
        digit.append(str(n % k))
        n = n // k
    return ''.join(reversed(digit))


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):  # num의 제곱근까지만 계산
        if num % i == 0:
            return False
    # 나머지 존재 X
    return True


def solution(n, k):
    answer = 0

    s = convert(n, k)  # 해당 진법
    print(s)
    p = re.split("0+", s)
    print(p)
    for prime in p:
        if prime:
            if isPrime(int(prime)):
                answer += 1

    return answer
