import sys
sys.stdin = open('input.txt')


def bfs(k):
    global ans

    q = []
    vsted = [False] * (V + 1)

    vsted[k] = True
    q.append(k)
    while q:
        i = q.pop(0)
        ans.append(i)
        for j in arr[i]:
            if not vsted[j]:
                vsted[j] = True
                q.append(j)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    arr = [[] for _ in range(V + 1)]
    for _ in range(E):
        i, j = map(int, input().split())
        arr[i].append(j)
        arr[j].append(i)

    ans = []

    bfs(1)
    ans = ' '.join(map(str, ans))

    print(f'#{tc} {ans}')
