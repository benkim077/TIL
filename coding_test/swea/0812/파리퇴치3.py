import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = tuple(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    for i in range(N):
        for j in range(N):
            sm = 0
            sm += arr[i][j]
            for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                for mult in range(1, M):
                    ni = i + di * mult
                    nj = j + dj * mult
                    if 0 <= ni < N and 0 <= nj < N:
                        sm += arr[ni][nj]
            if mx < sm:
                mx = sm

    for i in range(N):
        for j in range(N):
            sm = 0
            sm += arr[i][j]
            for di, dj in ((-1, 1), (1, 1), (1, -1), (-1, -1)):
                for mult in range(1, M):
                    ni = i + di * mult
                    nj = j + dj * mult
                    if 0 <= ni < N and 0 <= nj < N:
                        sm += arr[ni][nj]
            if mx < sm:
                mx = sm

    print(f'#{tc} {mx}')
