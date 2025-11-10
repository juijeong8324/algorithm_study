# Input
# n = 컴퓨터 개수 (1 이상 200 이하)
# computers = 연결에 대한 정보가 담긴 2차원 배열 (0부터 n-1인 정수)
# # i번 - j번 컴퓨터 연결: computers[i][j] = 1, 즉 양방향임을 알 수 있음
# Output
# 네트워크의 개수
# # 네트워크란
# # A - B → B - C → C - A임! = A,B,C는 모두 같은 네트워크!
# Hint
# Union Find
# 같은 네트워크면 같은 노드 번호로
# 단, 시간 복잡도가 O(N^3)

def solution(n, computers):

    temp = []
    for i in range(n):
        temp.append(i)  # 초기 = 각자 자신의 노드 번호

    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                # i와 j 네트워크 합치기
                for k in range(n):
                    if temp[k] == temp[i]:  # k와 i가 같은 네트워크라면
                        temp[k] = temp[j]  # k의 네트워크(=i의 네트워크)를 j의 네트워크로 Union

    return len(set(temp))  # 중복 제거 후
