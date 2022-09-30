import sys
from collections import deque
sys.stdin = open('input.txt')
INF = 100000


def dijkstra(si, sj):
    distance = [[INF] * N for _ in range(N)]
    distance[si][sj] = 0
    q = deque()
    q.append((si, sj))

    while q:
        i, j = q.popleft()
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if distance[ni][nj] > distance[i][j] + data[ni][nj]:
                    distance[ni][nj] = distance[i][j] + data[ni][nj]
                    q.append((ni, nj))
    return distance[ei][ej]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    si, sj = 0, 0
    ei, ej = N - 1, N - 1

    ans = dijkstra(si, sj)

    print(f'#{tc} {ans}')