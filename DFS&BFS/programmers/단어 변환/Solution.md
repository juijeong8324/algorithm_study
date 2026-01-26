# 단어 변환

## 문제

- **Input**
  - begin, target, words(3개 ~ 50개, 중복되는 단어는 없다!!!!!!!!!!)
  - 모든 단어의 길이는 같다. begin과 target은 같지 않다.
- **Output**
  - 규칙에 따라 begin에서 target으로 변환하는 가장 짧은 변환 과정 횟수
  - 1. 한 번에 한 개의 알파벳만 바꿀 수 있다.
  - 2. words에 있는 단어로만 변환할 수 있다.
  - words에 없는 target이면 0 return

<br>
<br>

## Key point

**1. BFS**  
글자가 서로 1씩 차이나는 노드끼리 연결된 그래프가 있다 가정해보자.  
이때 BFS로 방문하면 최단거리!
![Alt text](image-2.png)

<br>

**2. 1씩 차이나는 글자를 확인하는 방법**

- **`main.py` 방법**

```python
    def check(target, words):  # 1씩 차이나는 단어 찾기
        diff_count = 0
        for a, b in zip(target, words):
            if a != b:
                diff_count += 1
            if diff_count > 1:
                return False

        return diff_count == 1
```

현재 단어와 words를 모두 순회한 word의 각 글자를 비교  
Time Complexity = O(N x N x L) = 모든 단어 방문 x 매 BFS마다 words 순회 x check 함수

🤔 그러나 현재는 words의 길이가 50개지만.. 10억개라면??

<br>

- **`optimization.py` 방법**

```python
    words = set(words)  # 조회 시 O(1)

    while q:
        path += 1  # path 미리 업데이트
        for _ in range(len(q)):
            cur, path = q.popleft()

            for i in range(len(cur)):  # 현재 단어의 각 위치에 대해서
                for c in 'abcdefghijklmnopqrstuvwxyz':  # a-z를 순회하며 변환
                    next = cur[:i] + c + cur[i+1:]

                if next in words and next not in vis: # 체크
```

현재 단어에서 각 글자를 a~z로 변환  
Time Complexity = O(N x L x 26) = words 길이 x 단어의 길이 x 26
