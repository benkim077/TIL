import sys
sys.stdin = open('input.txt')

di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]

# mt: 산
# i, j 좌표
# flag: 땅파기 사용 했는지 안했는지
# length: 경로 길이
# vsted: 방문 체크
def bt(mt, i, j, flag, length, vsted):
    global N, K, mx
    # 길이 최댓값 저장
    if mx < length:
        mx = length

    # 하부함수 호출
    for k in range(4):                              # delta search
        ni, nj = i + di[k], j + dj[k]
        if 0<=ni<N and 0<=nj<N and not vsted[ni][nj]:   # 범위 안 벗어나고, 방문 안한 경우만
            if mt[ni][nj] < mt[i][j]:                       # 경사 OK
                vsted[ni][nj] = True
                bt(mt, ni, nj, flag, length + 1, vsted)
                vsted[ni][nj] = False
            else:                                           # 경사 not OK
                if not flag:                                    # 땅파기 안 사용한 경우, 사용함
                    temp = mt[ni][nj] - mt[i][j]
                    if temp < K:                                    # 땅파기 가능성 체크. 호출 전 후로, mt, flag, vsted 바꿨다가 되돌려놓기
                        mt[ni][nj] -= temp + 1
                        flag = True
                        vsted[ni][nj] = True
                        bt(mt, ni, nj, flag, length + 1, vsted)
                        mt[ni][nj] += temp + 1
                        flag = False
                        vsted[ni][nj] = False
    

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mt = [list(map(int, input().split())) for _ in range(N)]

    # start point => lst
    mx = 0
    lst = []
    for i in range(len(mt)):
        temp = max(mt[i])
        if mx < temp:
            mx = temp
    for i in range(N):
        for j in range(N):
            if mt[i][j] == mx:
                lst.append((i, j))
    
    # 백트래킹으로 길이 찾기
    vsted = [[False] * N for _ in range(N)]
    mx = 0
    for ele in lst:
        vsted[ele[0]][ele[1]] = True
        bt(mt, ele[0], ele[1], False, 1, vsted) # mt, i, j, flag, length, vsted
        vsted[ele[0]][ele[1]] = False

    print(f'#{tc} {mx}')