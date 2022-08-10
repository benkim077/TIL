# 2차원 배열

## 2차원 배열 선언

- 1차원 배열을 묶어놓은 배열

- `arr = [[0, 1, 2, 3][4, 5, 6, 7]]`

### 입력값을 2차원 배열에 넣기

```python
'''
Input
3
1 2 3
4 5 6
7 8 9
'''
# List Comprehension 활용
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
```

## 2차원 배열 접근

### n X m 배열의 모든 원소에 접근하기

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

### 델타를 이용한 2차원 배열 탐색

- 2차 배열의 한 좌표에서 4방향 인접 배열 요소 탐색하는 방법

- 이웃하는 칸이 어떻게 변하는가?

    - 상우하좌

        - 상 i - 1, j + 0

        - 우 i + 0, j + 1

        - 하 i + 1, j + 0

        - 좌 i + 0, j - 1

    - di = [-1, 0, +1, 0]

    - dj = [0, +1, 0, -1]

- 반복문 으로 주변 칸 탐색

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

### 전치 행렬

- `arr[i][j], arr[j][i] = arr[j][i], arr[i][j]`를 하면 된다.

### 2차원 배열 연습문제

```python
# 2차원 배열의 / 방향 대각선의 합 중 최댓값을 구해라.
s = [0]*(2*N - 1)
for i in range(N):
    for j in range(N):
        s[i + j] += arr[i][j] # / 방향 대각선의 공통되는 특징을 생각해보세요.
print(s)
```