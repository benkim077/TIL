import sys
sys.stdin = open('input.txt')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = 3
N = 100

for _ in range(1, T+1):
    tc = int(input())
    arr = [([-1] + list(map(int, input().split())) + [-1]) for _ in range(N)] + [[-1] * (N+2)]

    for start in range(1, N+1):
        i, j = 0, start
        direction = 1  # 0, 1, 2, 3 = 상 우 하 좌
        while True:
            # 현재 위치 값 확인
            if arr[i][j] == 1:
                pass
            elif arr[i][j] == -1:
                break
            elif arr[i][j] == 0:
                break
            elif arr[i][j] == 2:
                break

            # 방향 전환 필요?
            if direction == 1:
                if arr[i + di[2]][j+dj[2]] == 1 or arr[i + di[2]][j+dj[2]] == 2:
                    direction = (direction + 1) % 4
            elif direction == 2:
                if arr[i + di[1]][j+dj[1]] == 1 or arr[i + di[1]][j+dj[1]] == 2:
                    direction = (direction - 1) % 4
                elif arr[i + di[3]][j+dj[3]] == 1 or arr[i + di[3]][j+dj[3]] == 2:
                    direction = (direction + 1) % 4
            elif direction == 3:
                if arr[i + di[2]][j + dj[2]] == 1 or arr[i + di[2]][j + dj[2]] == 2:
                    direction = (direction - 1) % 4

            # 이동하기
            if direction == 1:
                i = i + di[1]
                j = j + dj[1]
            elif direction == 2:
                i = i + di[2]
                j = j + dj[2]
            elif direction == 3:
                i = i + di[3]
                j = j + dj[3]

        ans = -1
        if arr[i][j] == 2:
            ans = start - 1
            print(f'#{tc} {ans}')
            break
