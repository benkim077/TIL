def prim2(r, V):
    MST = [0] * (V + 1)
    MST[r] = 1
    s = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V + 1):
            if MST[i] == 1:
                for j in range(V + 1):
                    if adj_arr[i][j] > 0 and MST[j] == 0 and minV > adj_arr[i][j]:
                        u = j
                        minV = adj_arr[i][j]
        s += minV
        MST[u] = 1
    return s


V, E = map(int, input().split())
adj_arr = [[0]*(V + 1) for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj_arr[u][v] = w
    adj_arr[v][u] = w

print(prim2(0, V))
