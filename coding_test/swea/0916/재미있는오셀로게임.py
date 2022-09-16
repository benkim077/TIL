import sys
sys.stdin = open('input.txt')
di, dj = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def solve(i, j, d):
    global color, cnt1b, cnt2w

    # if board[i][j] == 0:
    #     board[i][j] = color
    # elif board[i][j] != color:
    #     board[i][j] = color
    # else:
    #     return

    ni, nj = i + di[d], j + dj[d]
    if 0 <= ni < N and 0 <= nj < N:
        if board[ni][nj] == 0:
            return
        elif board[ni][nj] == color:
            return
        elif board[ni][nj] != color:
            board[ni][nj] = color
            solve(ni, nj, d)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    board = [[0] * N for _ in range(N)]
    # 1: Black, 2: White
    board[N // 2][N // 2] = 2
    board[N // 2][N // 2 - 1] = 1
    board[N // 2 - 1][N // 2] = 1
    board[N // 2 - 1][N // 2 - 1] = 2


    for _ in range(M):
        j, i, color = map(int, input().split()) # 1 2 1
        i, j = i - 1, j - 1

        board[i][j] = color
        for d in range(8):
            solve(i, j, d)

        print(i, j, board)

    cnt1b, cnt2w = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt1b += 1
            elif board[i][j] == 2:
                cnt2w += 1

    print(cnt1b, cnt2w)