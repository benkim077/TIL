def dfs(start):
    stk = []
    vsts = [0] * (V + 1)

    v = start
    vsts[v] = 1
    sols.append(v)

    while True:
        for w in range(1, V + 1):
            if adj[v][w] == 1 and vsts[w] == 0:
                stk.append(v)
                v = w
                vsts[w] = 1
                sols.append(w)
                break
        else:
            if stk:
                v = stk.pop()
            else:
                break


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = list([0]*(V + 1) for _ in range(V + 1))
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s][e] = adj[e][s] = 1

    sols = []
    dfs(1)

    print(f'#{tc}', *sols)
