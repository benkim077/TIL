import sys
sys.stdin = open('input.txt')

pwd = {
    0:[0,0,0,1,1,0,1],
    1:[0,0,1,1,0,0,1],
    2:[0,0,1,0,0,1,1],
    3:[0,1,1,1,1,0,1],
    4:[0,1,0,0,0,1,1],
    5:[0,1,1,0,0,0,1],
    6:[0,1,0,1,1,1,1],
    7:[0,1,1,1,0,1,1],
    8:[0,1,1,0,1,1,1],
    9:[0,0,0,1,0,1,1],
}
def get_sp():
    global si, sj

    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                si = i
                sj = j + 56
                return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, list(input()))) for _ in range(N)]

    si, sj = 0, 0
    # 위치찾기1
    get_sp()    # starting_point 찾기

    # 위치찾기2
    for j in range(sj, -1, -1):
        if j < M:
            if data[si][j] == 1:
                sj = j
                break
    sj = sj - 56 + 1
    # print(si, sj)   # 6, 69

    pwd_code = []
    for j in range(8):
        nj = sj + j * 7
        for k in range(10):
            if pwd[k] == data[si][nj: nj + 7]:
                pwd_code.append(k)

    # print(pwd_code)
    sm = 0
    for i in range(8):
        if i % 2:
            sm += pwd_code[i]
        else:
            sm += pwd_code[i] * 3

    if sm % 10 == 0:
        ans = sum(pwd_code)
    else:
        ans = 0

    print(f'#{tc} {ans}')
