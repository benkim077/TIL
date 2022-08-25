import sys
sys.stdin = open('input.txt')


def bfs(v):
    global ans, G
    vsted = [0] * (V + 1)
    q = []

    vsted[v] = 1
    q.append(v)

    while q:
        t = q.pop(0)
        if vsted[G]:
            ans = vsted[G] - 1
            return

        for w in adj[t]:
            if not vsted[w]:
                vsted[w] = vsted[t] + 1
                q.append(w)



T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
    S, G = map(int, input().split())

    ans = 0
    bfs(S)

    print(f'#{tc} {ans}')
