import sys
sys.stdin = open('input.txt')


def dfs(ni, nj) -> None:
    global ei, ej, ans, N, data
    # 종료 조건
    if ni == ei and nj == ej:               # 목표에 도달한 경우 종료
        ans = 1
        return

    if not (0 <= ni < N and 0 <= nj < N):   # 인덱스를 벗어나는 경우 종료
        return

    if data[ni][nj] == 1:                   # 막다른 길인 경우 종료
        return

    # 하부 함수 호출



dij = [(-1, 0), ()]  # 상 우 하 좌


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    # 2, 3 위치 찾기. start i and j. end i and j
    for i in range(N):
        for j in range(N):
            if data[i][j] == 3:
                ei = i
                ej = j
            if data[i][j] == 2:
                si = i
                sj = j

    ans = 0

    dfs(si, sj)

    print(f'#{tc} {ans}')
