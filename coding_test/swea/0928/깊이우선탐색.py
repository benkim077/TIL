import sys
sys.stdin = open('input.txt')


def dfs(k):
    global cnt

    ans_lst[cnt] = k
    cnt += 1
    vsted[k] = True

    for w in adj_lst[k]:
        if not vsted[w]:
            dfs(w)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj_lst = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj_lst[s].append(e)
        adj_lst[e].append(s)

    for i in range(1, V + 1):
        adj_lst[i].sort()

    ans_lst = [0] * (V)
    cnt = 0
    vsted = [0] * (V + 1)
    dfs(1)

    print(f'#{tc}', end=' ')
    print(*ans_lst)