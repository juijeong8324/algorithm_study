# 1로 만들기

### Key Point

- **BFS**  
  BFS에서 첫 번째 방문은 최단 거리임읇 보장하기 때문에  
  **N 노드를 처음 방문** = **최소 연산 횟수(거리)로 도달**

```python
    from collections import deque

    N = int(input())
    dist = [0 for _ in range(N+1)]  # How many operations to reach?
    q = deque()  # queue

    q.append(1)
    dist[1] = 0

    while q:
        currN = q.popleft()

        if currN == N:
            break

        # currN * 2 (역연산: N / 2)
        if currN * 2 <= N and dist[currN * 2] == 0:
            dist[currN * 2] = dist[currN] + 1
            q.append(currN * 2)

        # currN * 3 (역연산: N / 3)
        if currN * 3 <= N and dist[currN * 3] == 0:
            dist[currN * 3] = dist[currN] + 1
            q.append(currN * 3)

        # currN + 1 (역연산: N - 1)
        if currN + 1 <= N and dist[currN + 1] == 0:
            dist[currN + 1] = dist[currN] + 1
            q.append(currN + 1)

    print(dist[N])

```

<br>

- DP  
  N의 최소 연산 횟수는 N/3, N/2, N-1의 최소 연산 횟수에 1을 더한 것과 같기 때문!

<br>

### Algorithm Approach: DP

1. **Define DP table**

```
    D[i] = i를 1로 만들기 위해 필요한 연산 사용 횟수의 최솟값
```

<br>

2. **Find Recurrence relation**

```
D[k] = min(D[k/3)+1, D[k/2]+1, D[k-1]+1)
```

<br>

3. **초기값**

```
D[1] = 0
```
