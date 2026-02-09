# 단속 카메라

## 문제

- **Input**
  - `routes` = 고속도로를 이동하는 차량의 경로
    - `routes[i][0]` = i번째 차량이 고속도로에 진입한 지점
    - `routes[i][1]` = i번째 차량이 고속도로에서 나간 지점
    - 진입/진출 지점 = -30,000 ~ 30,000
    - 진입/진출 지점에 설치되어 있어도 카메라를 만난 것으로 간주
    - 차량 수 = 1 ~ 10,000

- **Output**  
  모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치?

<br>
<br>

## Key point

- **Greedy**
  - 겹치는 구간 중 **가장 빨리 끝나는 차량의 진출점(`end`)**에 카메라 설치

<br>

- Q. 왜 진입점을 기준으로 정렬하면 틀리냐?  
   A. 그리디 기준은 “가장 빨리 끝나는 차량의 진출 지점” 이다.
  A. 진입점 기준으로 정렬 시, 진입은 빠른데 진출이 느린 차량의 경우에 더 빨리 끝나는 차량의 구간을 포함하지 못한 위치에 카메라 설치하게 됨.
  ![alt text](image.png)

<br>
<br>

## Algorithm Approach

1. **진출점(`routes[i][1]`)** 를 기준으로 정렬

```python
routes.sort(key = lambda x: x[1])
```

2. 현재 가장 빠른 진출점과 현재 차량의 진입점이 겹치는지 확인 후 count

```python
  last_camera = float('-inf')
  for start, end in routes:
        if start > last_camera: # 겹치지 않는다면
            last_camera = end # 새로운 진출점 update
            answer += 1 # 새로운 카메라 추가
```
