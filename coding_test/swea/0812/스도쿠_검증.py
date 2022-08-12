import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1

    for i in range(9):
        for j in range(9):
            if i % 3 == 0 and j % 3 == 0:
                sm = 0
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        sm += arr[m][n]
                if sm == 45:
                    pass
                else:
                    ans = 0

    for i in range(9):
        sm = 0
        for j in range(9):
            sm += arr[i][j]
        if sm == 45:
            pass
        else:
            ans = 0

    for j in range(9):
        sm = 0
        for i in range(9):
            sm += arr[i][j]
        if sm == 45:
            pass
        else:
            ans = 0

    print(f'#{tc} {ans}')
