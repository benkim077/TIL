INF = 10 * 50

def dijkstra(s):
    D = adj_arr[s][:]
    v = [0] * N
    v[s] = 1

    for _ in range(N - 1):
        mn, i_min = INF, 0
        for i in range(N):
            if v[i] == 0 and mn > D[i]:
                i_min, mn = i, D[i]
        v[i_min] = 1

        for i in range(N):
            D[i] = min(D[i], D[i_min] + adj_arr[i_min][i])

    return D[N - 1]

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj_arr = [[INF] * N for _ in range(N)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_arr[s][e] = w
    for i in range(N):
        adj_arr[i][i] = 0

    ans = dijkstra(0)

    print(f'#{tc} {ans}')

