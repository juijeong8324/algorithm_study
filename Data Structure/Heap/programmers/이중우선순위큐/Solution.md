# 이중우선순위큐

## 문제

- **이중 우선순위 큐란?**  
  우선 순위 큐에서 최댓값과 최솟값을 삭제할 수 있는 연산을 할 수 있는 자료구조

- **Input**
  - operations = 이중 우선순위 큐가 할 연산 = 길이가 (1, 1,000,000) 인 문자열 배열
  - 연산
    - I 숫자 = 큐에 주어진 숫자 삽입
    - D 1 = 큐에서 최댓값 삭제
    - D -1 = 큐에서 최솟값 삭제
- **Output**
  - 모든 연산 처리 후 큐가 비어있으면 [0,0] 않으면 [최댓값, 최솟값]

<br>

## Key point

Max Heap과 Min Heap을 사용.
이때 동기화에 필요한 count 배열이 필요하다.

<br>

> ### 🤔 Heap
>
> ![Alt text](image.png)
>
> - Max 값과 Min 값을 찾아내기 위해 고안된 **Complete Binary Tree**
> - 트리 계층 구조를 가지지만 내부적으로 **Array**를 사용함.
>
> - 종류
>   - **Max Heap**: 부모 노드의 값이 자식 노드의 값보다 크거나 같은 경우.
>   - **Min Heap**: 부모 노드의 값이 자식 노드의 값보다 작거나 같은 경우.
> - 시간 복잡도  
>   insert, delete 모두 **O(log N)**, 트리의 최대 높이만큼 비교
>
> 하지만 같은 level의 노드끼리의 대소관계는 중요하지 않다. 오직 부모만!!

<br>
 
## Algorithm Approach

최대값 삭제인 경우 `maxHeap`에서 pop  
최솟값 삭제인 경우 `minHeap`에서 pop

이때 `count`: 숫자의 횟수를 저장하는 dict를 활용하여 동기화.

1. **삭제 전 동기화**

`maxHeap` 혹은 `minHeap`에서 이미 삭제된 원소일 수 있으므로 `count`로 확인해준다.

```python
  while maxHeap and count[-maxHeap[0]] == 0:
    heapq.heappop(maxHeap)
```

<br>

2. **빈 heap 체크 후 삭제**

```python
  if maxHeap:
      count[-maxHeap[0]] -= 1
      heapq.heappop(maxHeap)
```
