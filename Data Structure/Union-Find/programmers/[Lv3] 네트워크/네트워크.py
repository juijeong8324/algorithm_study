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

# 1. 정석 Union Find 버전
def solution(n, computers):
    parent = list(range(n))

    def find(x):
        if parent[x] != x:  # 자기 자신이 root가 아님
            parent[x] = find(parent[x])  # Path Compression

        return parent[x]

    def union(a, b):  # Merge
        a_root = find(a)
        b_root = find(b)

        if a_root != b_root:  # a_root의 부모를 b_root로 바꾸기
            parent[a_root] = b_root

    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                union(i, j)  # 같은 네트워크로 합치기

    return len(set(find(i) for i in range(n)))  # Path Compression 안 되는 경우를 방지

# 2. 간단한 버전
# 같은 네트워크면 같은 노드 번호로
# 단, 시간 복잡도가 O(N^3) == 비효율적!!


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
