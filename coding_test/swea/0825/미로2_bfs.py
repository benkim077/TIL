import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs(graph, si, sj, vsted):
    q = deque([(si, sj)])
    vsted[si][sj] = True

    while q:
        vi, vj = q.popleft()

        global ei, ej, ans
        if (vi, vj) == (ei, ej):
            ans = 1

        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            i, j = vi + di, vj + dj
            if 0 <= i < N and 0 <= j < N and not vsted[i][j]:
                q.append((i, j))
                vsted[i][j] = True


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
    bfs(graph, si, sj, vsted)

    print(f'#{tc} {ans}')
