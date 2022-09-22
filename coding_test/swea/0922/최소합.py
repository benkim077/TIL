import sys
sys.stdin = open('input.txt')


def bt(i, j, sm):
    global mn

    if i == N - 1 and j == N - 1:
        mn = min(mn, sm)
        return

    for (di, dj) in ((0, 1), (1, 0)):
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            if vsted[ni][nj] == 0:
                vsted[ni][nj] = sm + data[ni][nj]
            else:
                if vsted[ni][nj] <= sm + data[ni][nj]:
                    continue

            bt(ni, nj, sm + data[ni][nj])



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    si, sj = 0, 0
    ei, ej = N - 1, N - 1
    mn = (2 * (N - 1) + 1) * 10
    vsted = [[0] * N for i in range(N)]
    vsted[si][sj] = data[si][sj]
    bt(si, sj, data[si][sj])    # si, sj, sm
    print(f'#{tc} {mn}')
