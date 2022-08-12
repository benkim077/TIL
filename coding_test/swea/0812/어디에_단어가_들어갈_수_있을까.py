import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = tuple(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
            elif arr[i][j] == 1:
                cnt += 1
        if cnt == K:
            ans += 1

    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
            elif arr[i][j] == 1:
                cnt += 1
        if cnt == K:
            ans += 1

    print(f'#{tc} {ans}')
