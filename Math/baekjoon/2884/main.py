# Link : https://www.acmicpc.net/problem/2884
# 나의 풀이 

hour, min = map(int, input().split()) # map함수를 이용해서 space를 기준으로 문자열을 나누고 int형으로 바꾸어 각각 hour, min에 저장
result = min - 45
    
if result >= 0:   # 즉 min만 바꿔야 하는 경우
    print(hour, result) # 문자와 int 사이에 + 안 됨 ,로 구분! 그리고 자동으로 space 생기는 듯
else:  # hour를 바꿔야 하는 경우
    if(hour == 0): # 0시인 경우 23시로 바꿔야 함
        print(23,(60+ result)) # result가 음수이기 때문에 60을 더해주면 됨
    else:
        print(hour-1,(60 + result))
