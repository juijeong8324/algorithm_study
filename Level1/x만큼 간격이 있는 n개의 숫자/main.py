#Link : https://programmers.co.kr/learn/courses/30/lessons/12954?language=python3

## 첫번째 답 ##
def solution(x, n):
    answer = [] # 리스트 사용! 
    for i in range(1,n+1): #range()는 숫자를 갖는 객체! 즉 변수 i에 숫자 1부터 n까지(n+1은 안 센다) 값이 들어간다!
        answer.append(x*i) # 리스트에 요소를 추가!
    return answer
  
  
  ## 두번째 답 ##
  def solution(x, n):
    return [i * x + x for i in range(n)] #range(n)이면 0부터 n-1까지 포함하는 숫자 객체를 생성! 
    # 이러한 방법은 list comprehension 이라고 부른다!! 
    # 자세한 사용 방법은 https://blog.teamtreehouse.com/python-single-line-loops 참고!! 
