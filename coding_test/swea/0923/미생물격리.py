import sys
sys.stdin = open('input.txt')
# 7 2 9
# 1 1 7 1
direction_dict = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1),
}


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    data = [[0] * N for _ in range(N)]
    for _ in range(K):
        x, y, num, d = map(int, input().split())
        data[x][y] = [num, d]
    # print(data)

    n_data = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp = []
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):     # 상 하 좌 우
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and data[ni][nj] != 0:
                    if direction_dict[data[ni][nj][1]] == (di, dj):
                        temp.append((ni, nj, data[ni][nj][0], data[ni][nj][1]))

            sm = 0
            if len(temp) >= 1:
                for t in temp:
                    sm += t[2]
                if data[i][j] != 0:
                    # n_data[i][j][0] = sm

            if len(temp) >= 2:
                new_d = max(temp, key=lambda x:x[2])[3]
                if data[i][j] != 0:
                    # n_data[i][j][1] = new_d

    print(n_data)