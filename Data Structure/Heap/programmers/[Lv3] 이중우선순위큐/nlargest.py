# Input
# operations = 이중 우선순위 큐가 할 연산 
#            = 길이가 (1, 1,000,000) 인 문자열 배열 
# Output
# 모든 연산 처리 후 큐가 비어있으면 [0,0] 않으면 [최댓값, 최솟값]
# 명령어
# I 숫자 = 큐에 주어진 숫자 삽입
# D 1 = 큐에서 최댓값 삭제 
# D -1 = 큐에서 최솟값 삭제 
# heapq의 내장함수 nlargest 이용
# heapq는 최소힙으로 구현 

import heapq

def solution(operations):
    heap = []
    
    for o in operations:
        I, num = o.split()
        if I == "I":
            heapq.heappush(heap, int(num))
        else:
            if len(heap) == 0:
                continue
            elif int(num) == 1:
                # 가장 큰 1개의 요소가 담긴 리스트를 반환 
                # 해당 요소의 index를 구하고 heap 리스트에서 삭제
                heap.pop(heap.index(heapq.nlargest(1, heap)[0])) 
            else: # 기본적으로 최소 힙
                heapq.heappop(heap)
                
    if len(heap):
        return [heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]]
    else:
        return [0,0]