import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # 도시의 크기, 집 하나 수익
    data = [list(map(int, input().split())) for _ in range(N)]

    home_lst = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                home_lst.append((i, j))

    mx = 0
    for i in range(N):
        for j in range(N):
            for k in range(1, N + 2):
                cnt = 0
                for ele in home_lst:
                    if abs(ele[0] - i) + abs(ele[1] - j) <= k - 1:
                        cnt += 1
                cost = k * k + (k - 1) * (k - 1)
                if cost <= cnt * M:
                    mx = max(mx, cnt)

    print(f'#{tc} {mx}')


