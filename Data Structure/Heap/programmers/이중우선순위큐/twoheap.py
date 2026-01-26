import heapq
from collections import defaultdict  # dict의 keyError 방지


def solution(operations):
    minHeap = []
    maxHeap = []
    count = defaultdict(int)  # num: 횟수

    for o in operations:
        I, num = o.split()
        if I == "I":
            heapq.heappush(minHeap, int(num))
            heapq.heappush(maxHeap, -int(num))
            count[int(num)] += 1
        else:  # D
            if int(num) == 1:  # 최댓값 삭제
                # 동기화: 현재 top이 최소힙에서 삭제 된 원소인 경우
                while maxHeap and count[-maxHeap[0]] == 0:
                    heapq.heappop(maxHeap)

                if maxHeap:  
                    count[-maxHeap[0]] -= 1
                    heapq.heappop(maxHeap)

            elif int(num) == -1:  # 최솟값 삭제
                # 동기화: 현재 top이 최대힙에서 삭제 된 원소인 경우
                while minHeap and count[minHeap[0]] == 0:
                    heapq.heappop(minHeap)

                if minHeap:
                    count[minHeap[0]] -= 1
                    heapq.heappop(minHeap)

    # 연산 처리 후
    while maxHeap and count[-maxHeap[0]] == 0:
        heapq.heappop(maxHeap)

    while minHeap and count[minHeap[0]] == 0:
        heapq.heappop(minHeap)

    if minHeap and maxHeap:
        return [-heapq.heappop(maxHeap), heapq.heappop(minHeap)]
    else:
        return [0, 0]
