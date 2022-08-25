import sys
sys.stdin = open('input.txt')


def dfs(graph, vi, vj, vsted):
    vsted[vi][vj] = True

    global ei, ej, ans
    if vsted[ei][ej]:
        ans = 1

    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        i = vi + di
        j = vi + di
        if 0 <= i < N and 0 <= j < N and graph[i][j] != 1 and not vsted[i][j]:
            dfs(graph, i, j, vsted)


N = 16
T = 10
for _ in range(T):
    tc = int(input())
    graph = [list(map(int, list(input()))) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                si, sj = i, j
            if graph[i][j] == 3:
                ei, ej = i, j

    vsted = [[False] * N for _ in range(N)]

    ans = 0
    dfs(graph, si, sj, vsted)

    print(f'#{tc} {ans}')
