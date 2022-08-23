# '가능'한 모든 경우
    # n은 행 번호
    # 트리를 만들 때 일반화해서 적어야 한다.

import sys
sys.stdin = open('input.txt')


def get_row_value(i, j):
    global N, data, sm, sm_lst, vsted

    if i >= 0:
        sm += data[i][j]
        print(i, j, data[i][j])

    # 종료 조건
    if i == N - 1:
        sm_lst.append(sm)
        return

    # 하부 함수 호출
    for j in range(N):  # 0, 1, 2
        get_row_value(i + 1, j)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)

    sm = 0
    sm_lst = []
    vsted = [[0] * N for _ in range(N)]
    get_row_value(-1, 0)

    print(sm_lst)