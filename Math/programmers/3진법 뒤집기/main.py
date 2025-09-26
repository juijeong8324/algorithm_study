#Link : https://programmers.co.kr/learn/courses/30/lessons/68935

## 나의 방법 ##
def solution(n):
    answer = 0
    list = []

    while n != 0: 
        list.append(n%3) # 자릿수가 바뀌어서 저장되는 건 동일
        n = n//3

    k = 1;
    for i in reversed(range(len(list))): # 이때 list 0번째 부터(낮은 자릿수) 나오니까 거꾸로 reversed 해줘야 함..
        answer += list[i] * k
        k *= 3

    return answer
  
  
  ## 다른 사람 풀이 ##
  def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3) # 정수로 변환할 값과 밑을 int(value, base)의 형태로 입력해줍니다
    return answer
