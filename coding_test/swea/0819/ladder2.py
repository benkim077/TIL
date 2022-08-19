import sys
sys.stdin = open('input.txt')

dij = [(-1, 0), (0, 1), (1, 0), (0, -1)]    # 상 우 하 좌 (i, j)


for _ in range(10):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    mn = 10000
    for start in range(100):
        direction = 2
        i = 0
        j = start
        cnt = 0
        if data[i][j] == 0:
            continue
        while i < 99:
            # 양옆 체크, 방향 전환
            if direction == 0:
                pass
            elif direction == 1:
                if 0 <= i + 1 < 100 and data[i + 1][j] == 1:
                    direction = 2
            elif direction == 2:
                if 0 <= j - 1 < 100 and data[i][j - 1] == 1:
                    direction = 3
                elif 0 <= j + 1 < 100 and data[i][j + 1] == 1:
                    direction = 1
            elif direction == 3:
                if 0 <= i + 1 < 100 and data[i + 1][j] == 1:
                    direction = 2
            # 이동
            if direction == 0:
                pass
            elif direction == 1:
                di, dj = dij[1]
                i += di
                j += dj
                cnt += 1
            elif direction == 2:
                di, dj = dij[2]
                i += di
                j += dj
            elif direction == 3:
                di, dj = dij[3]
                i += di
                j += dj
                cnt += 1
            # 범위를 넘어갔는지 체크
            if 0 <= i < 100 and 0 <= j < 100:
                pass
            else:
                break
        
        # 최솟값
        if mn > cnt:
            mn = cnt
            idx = start

    print(f'#{tc} {idx}')
#1 18
#2 96
#3 16
#4 5
#5 99
#6 0
#7 97
#8 0
#9 62
#10 3
