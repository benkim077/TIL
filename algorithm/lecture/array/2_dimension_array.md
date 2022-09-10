# 2차원 배열

## 2차원 배열(n X m)의 모든 원소에 접근하기

```python
# 기본
for i in range(n):
    for j in range(m):
        arr[i][j]

# 열 우선 순회
for j in range(n):
    for i in range(m):
        arr[i][j]

# 지그재그 순회
for i in range(n):
    for j in range(m):
        arr[i][j + (m-1-2*j) * (i%2)] 
        # 짝수행일 때는 arr[i][j], 
        # 홀수일 때는 arr[i][m-1-j]가 된다.

# 지그재그 순회 2
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            arr[i][j]
        else:
            arr[i][m-1-j]
```

## 델타 탐색

> 델타를 이용한 2차원 배열에서 인접 요소탐색

- 이웃하는 칸이 어떻게 변하는가?

    - 상 i - 1, j + 0

    - 우 i + 0, j + 1

    - 하 i + 1, j + 0

    - 좌 i + 0, j - 1

    - di = [-1, 0, +1, 0]

    - dj = [0, +1, 0, -1]

```python
di = [-1, 0, +1, 0]
dj = [0, +1, 0, -1]

for i in range(N):
    for j in range(M):
        for k in range(4):
            # 주변 칸 인덱스 ni, nj
            ni = i + di[k] 
            nj = j + dj[k]

            if 0<=ni<N and 0<=nj<M:
                print(ni, nj)
```

> 응용하면, 주변 8칸을 탐색할 수 있다.

> 바로 이웃만 아니라, n칸 떨어진 곳 까지 다 접근하고 싶다면? for d in range(1, 3): 이라는 반복문을 만들어주면 된다.

## 전치 행렬

```python
# m X n 행렬의 전치행렬(n X m 행렬) 만들기
m = len(arr)
n = len(arr[0])

t_arr = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        t_arr[i][j] = arr[j][i]
```

### 메서드를 이용한 전치행렬

`arr_T = list(zip(*arr))`는 arr의 전치행렬이다

## 2차원 배열 연습문제

- 2차원 배열의 / 방향 대각선의 합 중 최댓값을 구해라.

- / 방향 대각선의 **공통되는 특징**을 생각

```python
s = [0]*(2*N - 1)
for i in range(N):
    for j in range(N):
        s[i + j] += arr[i][j] 
print(s)
```