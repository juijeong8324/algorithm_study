# Link : https://www.acmicpc.net/problem/8958
# 나의 코드 

num = int(input()) # input(str 타입)을 int로 변환
score = [0 for i in range(num)] # 리스트 초기화 

for i in range(num):
    n = 0
    problem = list(input()) # OX 문자열을 리스트로서 받기 
    for j in range(len(problem)):
        if problem[j] == 'O': 
           n += 1 
           score[i] = score[i] + n
        else:
           n = 0      # 0으로 초기화 

for i in range(num):
    print(score[i])
