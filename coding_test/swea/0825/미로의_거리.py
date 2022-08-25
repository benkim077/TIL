import sys
sys.stdin = open('input.txt')


def bfs(i, j):
    global ans
    vsted = [[0] * N for _ in range(N)]
    q = []

    pi, pj = i, j
    vsted[pi][pj] = 1
    q.append((pi, pj))

    while q:
        pi, pj = q.pop(0)

        if (pi, pj) == (ei, ej):
            ans = vsted[pi][pj] - 2
            return

        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni = pi + di
            nj = pj + dj
            if 0 <= ni < N and 0 <= nj < N and not vsted[ni][nj] and data[ni][nj] != 1:
                vsted[ni][nj] = vsted[pi][pj] + 1
                q.append((ni, nj))


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

    ans = 0

    bfs(si, sj)

    print(f'#{tc} {ans}')
