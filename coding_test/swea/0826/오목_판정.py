import sys
sys.stdin = open('input.txt')

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]


def solve(arr):
    for i in range(N):
        for j in range(N):
            for dir in range(8):
                temp = ''
                for k in range(5):
                    ni = i + di[dir] * k
                    nj = j + dj[dir] * k
                    if 0 <= ni < N and 0 <= nj < N:
                        temp += arr[ni][nj]
                if temp == 'ooooo':
                    return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    data = [(input()) for _ in range(N)]

    print(f'#{tc} {solve(data)}')
