# Input
# N = 시험장의 개수 (1 <= N <= 1,000,000)
# Ai = i번 시험장에 있는 응시자 수 (1 <= A_i <= 1,000,000)
# B, C = 총감독관에서 감시할 수 있는 응시자 수, 부감독관에서 감시할 수 있는 응시자 수 (1 <= B, C <= 1,000,000)
# 각 시험장에 총감독관은 오직 1명, 부감독관은 여려명 가능
# Output
# 각 시험장마다 응시생 모두 감시하기 위해서 필요한 감독관 수의 최솟값 

import sys
from collections import defaultdict, deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def main():
    N = int(input().strip())
    A = map(int, input().strip().split())
    B, C = map(int, input().strip().split())

    result = N 
    
    for r in A:
        r = r - B # 각 시험관에는 총감독관 1명이 감시하므로 
        if r > 0:
            result += (r + C - 1) // C # ceil: r = aC + b로 두고 생각해보자 

    print(result)

main()
