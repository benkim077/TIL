import sys
sys.stdin = open('input.txt')

di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]

def dfs(i, j, cnt):
    global mx, si, sj, ans_i, ans_j, vsted
    if mx == cnt:
        if data[si][sj] < data[ans_i][ans_j]:
            ans_i, ans_j = si, sj
    elif mx < cnt:
        mx = cnt
        ans_i, ans_j = si, sj

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and data[i][j] + 1 == data[ni][nj]:
            vsted[ni][nj] = True
            dfs(ni, nj, cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    ans_i, ans_j = 0, 0
    vsted = [[False] * N for _ in range(N)]

    for si in range(N):
        for sj in range(N):
            if vsted[si][sj] == True:
                continue
            vsted[si][sj] = True
            dfs(si, sj, 1)

    print(f'#{tc} {data[ans_i][ans_j]} {mx}')