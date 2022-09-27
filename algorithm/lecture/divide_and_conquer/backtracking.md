# 백트래킹

- 여러 가지 선택지(옵션)들이 존재하는 상황에서 한 가지를 선택한다.

- 선택이 이루어지면 새로운 선택지들의 집합이 생성된다.

- 이런 선택을 반복하면서 최종 상태에 도달한다.

    - 올바른 선택을 계속하면 목표 상태에 도달한다.

## 백트래킹과 dfs과의 차이

- 어떤 노드에서 출발하느 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도 횟수를 줄임(prunning, 가지치기)

- 깊이 우선 탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단

- dfs를 가하기에는 경우의 수가 너무 많음. 즉 n!가지의 경우의 수를 가진 문제에 대해 dfs를 사용하면 당연히 처리 불가능한 문제

- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간을 요하므로 처리 불가능

## N-Queens 문제

### 8-Queens 문제

- 후보 해의 수 64C8

- 실제 해의 수 : 92개

- 44억 개가 넘는 후보 해 중에서 92개를 최대한 효율적으로 찾아내는 것이 관건

### 4-Queens 문제

- 같은 행에 위치할 수 없다

- 모든 경우의 수 : 4 * 4 * 4 * 4 = 256

- 백트래킹 기법 적용

### 백트래킹 이용 알고리즘 진행 절차

1. 상태 공간 트리의 깊이 우선 탐색을 실시

2. 각 노드가 유망한지 점검

3. 유망하지 않다면, 그 노드의 부모 노드로 돌아가서 계속 검색

### 깊이 우선 검색 vs 백트래킹

- dfs => 155 노드

- bt => 27 노드

### n-queens 문제 코드 

#### 1 반복을 최소화하기 위한 코드

```python
def bt(k):
    global ans

    if k == N:
        ans += 1
        return

    for j in range(N):
        if check(k, j):
            board[k][j] = 1
            bt(k + 1)
            board[k][j] = 0


def check(si, sj):
    # 위쪽 체크
    for i in range(si):
        if board[i][sj]:
            return 0

    # 좌상 대각선 체크
    i, j = si - 1, sj - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return 0
        i, j = i - 1, j - 1

    # 우상 대각선 체크
    i, j = si - 1, sj + 1
    while i >= 0 and j < N:
        if board[i][j]:
            return 0
        i, j = i - 1, j + 1

    # 다 통과됐으면 1 리턴
    return 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    ans = 0
    board = [[0] * N for _ in range(N)]
    bt(0)
    print(f'#{tc} {ans}')
```

#### 2 di, dj를 이용한 코드

- di, dj를 이용해서 코드를 줄일 수 있지만, 시간은 오히려 늘어난다.

#### 3 lookup table을 이용한 풀이

```python
def dfs_tbl(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if j not in v1 and (n + j) not in v2 and (n - j) not in v3:
            v1.append(j), v2.append(n + j), v3.append(n - j)
            dfs_tbl(n + 1)
            v1.pop(), v2.pop(), v3.pop()

# v1, v2, v3 = [], [], []
# dfs_tbl(0)
```

- 오른쪽 대각선

    - 더하면 같은 값을 갖는 대각선

    - i + j를 vsted2에 저장

- 왼쪽 대각선

    - i - j가 같은 대각선을 나타낸다.

    - 파이썬에선 그냥 i - j 써도 된다.(? 다른 언어에서도 될 것 같은데.)

    - v3에 저장

- 위아래 선

    - j가 위아래 선을 타나낸다.

    - v1에 저장