import sys

sys.stdin = open('input.txt')

di = [-1, 0, 1, 0] # 상 우 하 좌
dj = [0, 1, 0, -1]

T = int(input())

for t in range(1, T+1):
    N = int(input())

    # -1로 둘러쌓인, 0으로 채워진 N*N 2차원 배열
    arr = [[-1]*(N+2)] + [[-1] + [0]*N + [-1] for _ in range(N)] + [[-1]*(N+2)]

    cnt = 1 # 카운트
    i = j = 1 # 인덱스로 사용할 변수
    dr = 1 # 방향


    while cnt <= N*N:
        # 0일 때만 값을 넣는다.
        if arr[i][j] == 0:
            arr[i][j] = cnt
            cnt += 1
        # 0이 아니면 직전 인덱스로 되돌아간다.
        else:
            i, j = i - di[dr], j - dj[dr]
            dr = (dr+1) % 4
        # 항상 다음 인덱스로 이동한다.
        i, j = i + di[dr], j + dj[dr]
    
    # 출력
    print(f'#{t}')
    for i in range(1,N+1):
        for j in range(1, N+1):
            print(arr[i][j], end=' ')
        print()
