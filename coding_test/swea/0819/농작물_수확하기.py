'''
범위를 잡아주는게 어려웠다.
아주 전형적인 문제.
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(input()) for _ in range(N)]

    sm = 0
    for i in range(N):
        if i < N // 2:
            for j in range(N // 2 - i, N // 2 + i + 1):
                sm += int(data[i][j])
        elif i > N // 2:
            for j in range(N // 2 - (N - i - 1), N // 2 + (N - i)):
                sm += int(data[i][j])
        else:
            for j in range(N):
                sm += int(data[i][j])

    print(f'#{tc} {sm}')
