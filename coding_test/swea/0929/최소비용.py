from collections import deque
INF = 11000


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
                temp = data[ni][nj] - data[i][j]
                if temp < 0:
                    temp = 0
                if distance[ni][nj] > distance[i][j] + temp + 1:
                    distance[ni][nj] = distance[i][j] + temp + 1
                    q.append((ni, nj))

    return distance[ei][ej]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    si, sj = 0, 0
    ei, ej = N - 1, N - 1

    print(f'#{tc} {dijkstra(si, sj)}')