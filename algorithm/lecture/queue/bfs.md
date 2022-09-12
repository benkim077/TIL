# BFS Breadth First Search 너비 우선 탐색

- 그래프 탐색 방법

- 시작점의 인접 정점들을 모두 차례로 방문하고, 방문했던 정점을 다시 시작점으로 하여 반복하는 방식

    - 인접 정점 탐색 후, 다시 BFS 진행해야 하므로, 큐 자료구조 활용(FIFO)

- BFS는 반복으로 구현한다.

## BFS 템플릿 및 코드

```
bfs(...)
[1] q, vsted[](, flag) 초기화
[2] 단위 작업
    - vsted 표시
    - q에 삽입(초기 데이터들)
    - 필요작업(solution 구하기)
while q: # q에 데이터가 있는 동안 작업함
[3] q에서 데이터 1개 꺼냄
    # 정답처리 필요시 비효율적이더라도 이 자리에서
[4] 4방향, 8방향, 연결된 노드 등 반복문을 돌면서
    조건에 맞는 경우 
        단위 작업(q에 삽입, vsted.. 등 위에 했던 것
```

```python
def BFS(G, v):              # 그래프 G, 시작점 v
    # 초기화
    vsted = [False] * (n + 1)   # n은 정점의 갯수. 
    q = []

    # 단위 작업
    vsted[v] = True
    q.append(v)

    while q:
        t = q.pop(0)
        visit(t)                # 정답 처리(정점 t에서 할 일)
        for i in G[t]:          # t와 연결된 모든 정점에 대해
            if not vsted[i]:        # 방문되지 않은 곳이라면
                vsted[i] = True
                q.append(i)             # 큐에 넣기
```

### 카운트 vsted 배열 만들기

- 마지막 처리에서 `vsted[j] = vsted[i] + 1` 이렇게 하면, **카운트 vsted 배열**을 만들 수 있다.(i는 시작 정점, j는 다음 정점)

    - vsted 배열에 **순서 정보**를 저장할 수 있다.

    - 처리 우선순위가 같은 것들을 모을 수 있다. 

    - 결과적으로 **출발지로부터 거리가 같은 것들을 모을 수 있다.**

    - 다양한 bfs 문제들을 해결할 수 있다.

## DFS와 BFS

- 최단경로를 찾는 문제는 DFS, BFS 둘 다 사용 가능하다

- DFS를 사용하고 싶다면, 가능한 모든 경로를 돌아봐야 한다.

    - 이것으로부터 얻을 수 있는 것은 '경로의 수'이다.

- DFS는 최단 거리 뿐만 아니라, 경로의 수, 경로 분석 등에 사용할 수 있다.

> 한 문제를 DFS, BFS로 둘 다 풀 수 있어야 한다.

### DFS로 경로의 수 세기

- 방문체크를 하기 때문에 경로가 겹치는 경우에는 안세진다. (이미 vsted == True)

- 방문체크를 안하면, 무한루프에 빠진다.

> 해결방법 : 진행방향으로 방문 표시를 했으니까, 리턴하기 전에 `vsted[i][j] = False`로 vsted에서 방문 표시를 지워준다.

### 경로 길이의 최솟값 찾기

```python
def dfs(i, j, s, N):                               # s를 이용해서 최솟값을 구해준다.
    global minV
    if maza[i][j] == 3:
        if minV > s + 1:
            minV = s + 1
        return
    else:
        vsted[i][j] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if maza[ni][nj] != 1 and vsted[ni][nj] == 0:
                dfs(ni, nj, s + 1, N)
        vsted[i][j] = 0                                     # 방문 표시를 지워주는 코드(경로 수 세는 경우)
        return
```

### 시작 지점이 여러개인 경우

> 가스가 퍼지는 예제, 다 퍼질 때까지 걸리는 시간을 구하라.

- BFS는 출발점이 2개 이상인 탐색도 가능하다.

- 시작 지점을 입력받지 않고, 시작 지점을 직접 찾아서 실행

- 도중에 끝나지 않게 함

```python
def bfs(N):
    vst
    q
    # 단위 작업
    for i in range(N):
        for j in range(N):
            if maza[i][j] == 2:
                q.append((i, j))    # 시작지점 큐에 넣고 시작
                vsted[i][j] = 1
    while q:                        # BFS 진행
        pass
```

## (정리) DFS, BFS 무엇을 사용할까?

- 탐색(빠짐없이, 중복없이) - DFS, BFS 둘 다 가능해야 한다.

- 최단거리 - 둘 다

- 경로의 수 - DFS

- 확산(출발이 여러 곳) - BFS