from collections import deque
import sys
sys.stdin = open('input.txt')

# bfs를 통해 거리를 계산
def bfs(i, j):
    q = deque()
    q.append((i, j))
    vsted[i][j] += 1
    while q:
        i, j = q.popleft()
        lst = get_way(i, j) # 현재 위치에서 연결할 수 있는 지점을 리턴하는 함수
        for ele in lst:
            q.append(ele)
            vsted[ele[0]][ele[1]] = vsted[i][j] + 1
    

di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]   # 델타 탐색에서 활용하는 변수
hashing = {                             # get_way함수에서 사용하는 dict
    # 10은 '1번 type에서 0번 방향으로 갔을 때'라는 뜻
    # value에 있는 list는 허용되는 타입을 의미
    # 즉, 타입과 방향을 알 때, 허용되는 타입들을 정리해놓은 dict
    '10': [1, 2, 5, 6], 
    '11': [1, 3, 6, 7],
    '12': [1, 2, 4, 7],
    '13': [1, 3, 4, 5],
    '20': [1, 2, 5, 6],
    '21': None,
    '22': [1, 2, 4, 7],
    '23': None,
    '30': None,
    '31': [1, 3, 6, 7], 
    '32': None,
    '33': [1, 3, 4, 5],
    '40': [1, 2, 5, 6],
    '41': [1, 3, 6, 7],
    '42': None,
    '43': None,
    '50': None,
    '51': [1, 3, 6, 7],
    '52': [1, 2, 4, 7],
    '53': None,
    '60': None,
    '61': None,
    '62': [1, 2, 4, 7],
    '63': [1, 3, 4, 5],
    '70': [1, 2, 5, 6],
    '71': None,
    '72': None,
    '73': [1, 3, 4, 5],
}

# 좌표를 입력하면 그 위치에서 갈 수 있는 다음 위치를 list로 리턴하는 함수
# 타입별로 방향을 구분해줬고, 나머지는 코드가 같음.
def get_way(i, j):
    lst = []
    type = tunnel[i][j]
    if type == 1:                       # 타입별로 구분해서 조건문
        for k in range(4):                  # 타입별로 방향 구분
            # 이하는 코드가 같음
            ni, nj = i + di[k], j + dj[k]
            key = str(type) + str(k)        # dict를 사용하기 위한 key 생성
            if 0 <= ni < N and 0 <= nj < M and not vsted[ni][nj] and tunnel[ni][nj] in hashing[key]:    # hashing dict를 사용해서 갈 수 있는지 체크
                lst.append((ni,nj))
    elif type == 2:
        for k in range(0, 3, 2):
            ni, nj = i + di[k], j + dj[k]
            key = str(type) + str(k)
            if 0 <= ni < N and 0 <= nj < M and not vsted[ni][nj] and tunnel[ni][nj] in hashing[key]:
                lst.append((ni,nj))
    elif type == 3:
        for k in range(1, 4, 2):
            ni, nj = i + di[k], j + dj[k]
            key = str(type) + str(k)
            if 0 <= ni < N and 0 <= nj < M and not vsted[ni][nj] and tunnel[ni][nj] in hashing[key]:
                lst.append((ni,nj))
    elif type == 4:
        for k in range(0, 2, 1):
            ni, nj = i + di[k], j + dj[k]
            key = str(type) + str(k)
            if 0 <= ni < N and 0 <= nj < M and not vsted[ni][nj] and tunnel[ni][nj] in hashing[key]:
                lst.append((ni,nj))
    elif type == 5:
        for k in range(1, 3, 1):
            ni, nj = i + di[k], j + dj[k]
            key = str(type) + str(k)
            if 0 <= ni < N and 0 <= nj < M and not vsted[ni][nj] and tunnel[ni][nj] in hashing[key]:
                lst.append((ni,nj))
    elif type == 6:
        for k in range(2, 4, 1):
            ni, nj = i + di[k], j + dj[k]
            key = str(type) + str(k)
            if 0 <= ni < N and 0 <= nj < M and not vsted[ni][nj] and tunnel[ni][nj] in hashing[key]:
                lst.append((ni,nj))
    elif type == 7:
        for k in range(0, 4, 3):
            ni, nj = i + di[k], j + dj[k]
            key = str(type) + str(k)
            if 0 <= ni < N and 0 <= nj < M and not vsted[ni][nj] and tunnel[ni][nj] in hashing[key]:
                lst.append((ni,nj))
    else:
        pass

    return lst


# main
T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    vsted = [[0] * M for _ in range(N)]
    
    # 갈 수 있는 위치를 검색
    bfs(R, C)

    # 0초과 L이하인 값만 카운트
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < vsted[i][j] <= L:
                cnt += 1

    # 출력
    print(f'#{tc} {cnt}')