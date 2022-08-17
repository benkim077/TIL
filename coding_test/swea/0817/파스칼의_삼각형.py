T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [[0]*(i + 1) for i in range(N)]

    for i in range(N):
        for j in range(i + 1):
            if j == 0 or j == len(arr[i]) - 1:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    print(f'#{tc}')
    for i in range(N):
        for j in range(i + 1):
            print(arr[i][j], end=' ')
        print()
