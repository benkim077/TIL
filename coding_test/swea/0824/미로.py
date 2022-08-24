import sys
sys.stdin = open('input.txt')


def bfs(ki, kj):
    vsted = [[0] * N for _ in range(N)]
    q = []

    vsted[ki][kj] = 1
    q.append((ki, kj))

    while q:
        i, j = q.pop(0)
        if (i, j) == (ei, ej):
            return 1

        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and data[ni][nj] != 1 and not vsted[ni][nj]:
                vsted[ni][nj] = vsted[i][j]
                q.append((ni, nj))

    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                si, sj = i, j
            if data[i][j] == 3:
                ei, ej = i, j

    ans = bfs(si, sj)

    print(f'#{tc} {ans}')
