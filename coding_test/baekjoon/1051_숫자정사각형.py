def solve():
    global ans

    # 시작 길이 찾기
    if N <= M:
        s_len = N
    else:
        s_len = M

    # 최대 정사각형 구하기
    while s_len > 0:
        range_i, range_j = N - s_len, M - s_len
        
        # 시작 위치 i, j
        for i in range(range_i + 1):
            for j in range(range_j + 1):
                
                # 델타 탐색
                if data_arr[i][j] == data_arr[i][j + s_len - 1] == data_arr[i + s_len - 1][j] == data_arr[i + s_len - 1][j + s_len - 1]:
                    # print(i, j, '에서 찾음!!')
                    ans = s_len
                    return
        s_len -= 1


N, M = map(int, (input().split()))
data_arr = [list(map(int, input())) for _ in range(N)]


ans = 0
solve()

print(ans**2)