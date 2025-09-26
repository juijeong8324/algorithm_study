# Link : https://programmers.co.kr/learn/courses/30/lessons/12950

## 나의 풀이 ##
def solution(arr1, arr2):
    answer = [] #answer[[]]로 생성하면 append 할 때 첫 번째 행으로 []가 생성 되어서 자꾸 에러가 뜬다! 그래서 []로 생성! 

    for i in range(len(arr1)): # 행 개수만큼 반복 
        line = [] # 빈 리스트 생성
        for j in range(len(arr1[0])): # 열 개수만큼 반복 
            line.append(arr1[i][j] + arr2[i][j]) #추가하고
        answer.append(line) # 한 행을 추가        

    return answer
  
  
  ## 다른 사람의 풀이 ##
  # Link : https://programmers.co.kr/learn/courses/30/lessons/12950/solution_groups?language=python3
  
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)] 
    # zip 함수는 두 그룹의 데이터를 서로 엮어주는 파이썬의 내장함수! 
    # a, b는 리스트(한 행)를 의미하고 c, d는 리스트 안의 요소를 의미하는 듯!
    return answer
  
# 아래는 테스트로 출력해 보기 위한 코드입니다.
# 출력값은 [[4,6], [7,9]]
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
