import sys

sys.stdin = open('input.txt')

for _ in range(2):
    tc = int(input())
    
    # 입력받기
    arr = []
    for _ in range(100):
        arr += [list(map(int, input().split()))]

    # mx
    mx = 0

    # 가로
    for i in range(100):
        sm = 0
        for j in range(100):
            sm += arr[i][j]
        if mx < sm:
            mx = sm

    # 세로
    for j in range(100):
        sm = 0
        for i in range(100):
            sm += arr[i][j]
        if mx < sm:
            mx = sm

    # 대각선
    for i in range(100):
        sm = 0
        sm += arr[i][i]
        if mx < sm:
            mx = sm

    for i in range(100):
        sm = 0
        sm += arr[i][99-i]
        if mx < sm:
            mx = sm

    # 출력
    print(f'#{tc} {mx}')