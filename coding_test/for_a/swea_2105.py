import sys
sys.stdin = open('input.txt')

di, dj = [-1, 1, 1, -1], [1, 1, -1, -1] # 대각선 방향 델타 탐색

def dfs(i, j, path, k):
    global si, sj, cnt

    if k == 3 and i == si and j == sj and len(path) >= 3:
        cnt = max(cnt, len(path))
        return

    if 0 <= i < N and 0 <= j < N and data[i][j] not in path:
        new_path = path + [data[i][j]]

        ni, nj = i + di[k], j + dj[k]
        dfs(ni, nj, new_path, k)

        if k < 3:
            ni, nj = i + di[k + 1], j + dj[k + 1]
            dfs(ni, nj, new_path, k + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]


    
    cnt = -1
    for si in range(N):
        for sj in range(N):
            dfs(si, sj, [], 0) # i, j에서 시작위치, 경로, 0은 방향

    print(cnt)