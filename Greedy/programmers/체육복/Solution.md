# 체육복

## 문제

- **Input**

  - `n``: 전체 학생 수 (2명~30명)
  - `lost``: 도난당한 학생들의 번호가 담긴 배열 (중복 x)
  - `reserve``: 여벌 체육복을 가져온 학생들의 번호가 담긴 배열 (중복 x)
  - 여벌 체육복을 가진 학생이 도난당했을 수 있다.
  - 이런 경우 다른 학생에게 체육복을 빌려줄 수 없다.

- **Output**  
  수업을 들을 수 있는 학생의 최댓값
  - 여벌의 옷을 가진 학생의 앞번호나 바로 뒷번호에게만 체육복을 빌려줄 수 있다.
  - 여벌 체육복을 가진 학생이 도난당했을 수 있다.
  - 이런 경우 다른 학생에게 체육복을 빌려줄 수 없다.

<br>
<br>

## Key point

- Greedy

  - **여벌 옷을 가진 학생들**을 기준으로 **앞 뒤**로 최대한 나눠준다.
  - 이때 여벌 옷을 최대한 남김없이 나눠주도록 하는 것이 핵심

- Sort
  - lost와 reserve가 오름차순 혹은 정렬되었다는 언급이 없다.
  - 여분의 옷은 앞뒤 학생에게 빌려줄 수 있기 때문에 `reserve`는 반드시 정렬되어야 한다.

<br>

## Algorithm Approach

```python
    def solution(n, lost, reserve):
        # lost와 reserve가 오름차순이라는 보장 없음
        # 여분의 옷이 있는 친구가 도난 당한 경우 확인
        r = [n for n in reserve if n not in lost]
        l = [n for n in lost if n not in reserve]

        # 반드시 정렬..
        r = sorted(r)

        # 여분 옷 있는 친구 기준으로
        for s in r:
            if s-1 in l: # 앞에 잃어버린 친구
                l.remove(s-1) # 빌렸으면 제거
            elif s+1 in l: # 뒤에 잃어버린 친구
                l.remove(s+1)
        return n - len(l)
```
