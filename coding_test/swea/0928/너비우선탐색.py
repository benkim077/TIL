from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(k):
    q = deque()
    q.append(k)
    vsted[k] = True

    while q:
        v = q.popleft()
        ans_lst.append(v)
        for w in range(1, V + 1):
            if adj_lst[v][w] == 1 and not vsted[w]:
                q.append(w)
                vsted[w] = True


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj_lst = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj_lst[s][e] = 1
        adj_lst[e][s] = 1

    ans_lst = []
    vsted = [False] * (V + 1)
    bfs(1)

    print(f'#{tc}', end=' ')
    print(*ans_lst)