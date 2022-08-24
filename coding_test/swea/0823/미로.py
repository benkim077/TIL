import sys
sys.stdin = open('input.txt')

di = [-1, 0, 1, 0]  # 상우하좌
dj = [0, 1, 0, -1]


def dfs(si, sj) -> None:
    stk = []
    vsted[si][sj] = True

    while True:
        for k in range(4):
            ni, nj = si + di[k], sj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and data[ni][nj] != 1 and not vsted[ni][nj]:
                stk.append((si, sj))
                si, sj = ni, nj
                vsted[si][sj] = True
                break
        else:
            if stk:
                si, sj = stk.pop()
            else:
                break


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 3:
                ei = i
                ej = j
            if data[i][j] == 2:
                si = i
                sj = j

    ans = 0

    vsted = [[False] * N for _ in range(N)]

    dfs(si, sj)

    print(f'#{tc} {int(vsted[ei][ej])}')
