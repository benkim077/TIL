import sys
sys.stdin = open('input.txt')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            ni = nj = -1
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni <= N-1 and 0 <= nj <= N-1:
                    absV = arr[i][j] - arr[ni][nj]
                    if absV < 0:
                        ans += -absV
                    else:
                        ans += absV


    print(f'#{t} {ans}')
