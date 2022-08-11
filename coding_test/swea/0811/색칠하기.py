import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 2 <= N <= 30

    # 0 으로 채워진 10*10 배열
    arr = [[0]*10 for _ in range(10)]

    for _ in range(N):
        lst = list(map(int, input().split()))

        # 빨강색이면 1(30^0)을 더하고, 파랑색이면 30(30^1)을 더한다.
        for i in range(lst[0], lst[2] + 1):
            for j in range(lst[1], lst[3] + 1):
                if lst[4] == 1:
                    arr[i][j] += 1
                elif lst[4] == 2:
                    arr[i][j] += 30

    cnt = 0
    for k in range(10):
        for l in range(10):
            # 30으로 나눈 나머지가 0보다 크면 빨강색으로 색칠된 것
            # 30으로 나눈 몫이 0보다 크면 파랑색으로 색칠된 것
            # 둘 다 만족하면 보라색
            if arr[k][l] % 30 > 0 and arr[k][l] // 30 > 0:
                cnt += 1

    print(f'#{tc} {cnt}')