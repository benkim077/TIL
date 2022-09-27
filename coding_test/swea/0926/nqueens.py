import sys
sys.stdin = open('input.txt')


def bt(k):
    global ans

    if k == N:
        ans += 1
        return

    for j in range(N):
        if check(k, j):
            board[k][j] = 1
            bt(k + 1)
            board[k][j] = 0


def check(si, sj):
    # 위쪽 체크
    for i in range(si):
        if board[i][sj]:
            return 0

    # 좌상 대각선 체크
    i, j = si - 1, sj - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return 0
        i, j = i - 1, j - 1

    # 우상 대각선 체크
    i, j = si - 1, sj + 1
    while i >= 0 and j < N:
        if board[i][j]:
            return 0
        i, j = i - 1, j + 1

    # 다 통과됐으면 1 리턴
    return 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    ans = 0
    board = [[0] * N for _ in range(N)]
    bt(0)
    print(f'#{tc} {ans}')