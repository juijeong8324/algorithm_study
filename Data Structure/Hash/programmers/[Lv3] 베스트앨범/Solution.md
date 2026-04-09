# 베스트 앨범

## 문제

- **Input**
  - `genres` = 노래의 장르를 나타내는 문자열 배열
    - `genres[i]` = 고유번호 i인 노래의 장르
    - 길이: 1 이상 10,000 이하 (= `plays`와 동일)
    - 장르 종류는 100개 미만
  - `plays` = 노래별 재생 횟수를 나타내는 정수 배열
    - `plays[i]` = 고유번호 i인 노래의 재생 횟수
  - 모든 장르는 장르 내 총 재생 횟수가 다르다
  - 장르에 속한 곡이 하나라면 하나의 곡만 수록

- **Output**  
  베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return
  - 수록 기준
    1. 속한 노래의 총 재생 횟수가 많은 장르 먼저 수록
    2. 장르 내에서 많이 재생된 노래 먼저 수록
    3. 재생 횟수가 같은 경우 고유 번호가 낮은 노래 먼저 수록

<br>
<br>

## Key point

- **dict (hash table)** 사용
  - 장르별 총 재생 횟수 저장 → `defaultdict(int)`
  - 장르별 노래 목록 저장 → `defaultdict(list)` + `heapq`

<br>

- **heapq** 는 자료구조가 아니라 list를 힙처럼 다루는 함수 모음
  - `heappush(heap, item)` / `heappop(heap)`
  - 최소 힙이 기본 → 최대 힙은 **음수 트릭** 사용

<br>

- Q. dict는 바로 sort 가능한가?  
  A. `dict.sort()` 없음! `sorted(d.items(), key=..., reverse=True)` 사용해야 함
  A. 또한 sorted는 key만 iterate하기 때문에 value 기준 정렬 불가.. 따라서 value에 접근하기 위해서 `d.items()` 로 변환해서 (key, value) 튜플로 iterate 하게 접근한다.

<br>

- Q. heapq에 `(play, idx)` 넣을 때 왜 `-play`?  
  A. heapq는 최소 힙이라 재생 횟수가 큰 게 먼저 나오려면 음수로 저장해야 함

<br>
<br>

## Algorithm Approach

1. 장르별 총 재생 횟수 & 노래 목록 저장  
   `(-play, idx)` 형태로 heappush → 최대 힙 효과

```python
for idx, (genre, play) in enumerate(zip(genres, plays)):
    genres_play[genre] += play
    heapq.heappush(genres_list[genre], (-play, idx))  # 최대힙
```

<br>

2. 장르를 총 재생 횟수 기준으로 정렬

```python
new_dict = sorted(genres_play.items(), key=lambda x: x[1], reverse=True)
```

<br>

3. 정렬된 장르 순서로 최대 2곡씩 추가

```python
for genre, play in new_dict:
    for _ in range(2):
        if genres_list[genre]:
            _, idx = heapq.heappop(genres_list[genre])
            answer.append(idx)
```
