# A ~ G 정점 -> 0 ~ 6
adjList = [[1, 2],      # 0
           [0, 3, 4],   # 1
           [0, 4],      # 2
           [1, 5],      # 3
           [1, 2, 5],   # 4
           [3, 4, 6],   # 5
           [5]]         # 6


def dfs(v, N):  # 시작 위치, 정점 갯수
    top = -1

    print(v)            # 방문하기 전 할 일

    visited[v] = 1      # 시작점 방문 표시
    while True:
        for w in adjList[v]:
            if visited[w] == 0:
                top += 1            # push(v)
                stk[top] = v
                v = w
                visited[w] = 1
                print(v)            # 방문해서 할 일이 적힐 코드
                break
        else:
            if top != -1:           # stk이 비어있지 않은 경우
                v = stk[top]
                top -= 1
            else:                   # 스택이 비어있으면
                break               # 이 break는 while을 중단시킴


N = 7
visited = [0] * N   # visited 생성
stk = [0] * N       # stack 생성

dfs(1, N)
