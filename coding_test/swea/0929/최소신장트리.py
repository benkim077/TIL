def find_set(x):
    while x != tree[x]:
        x = tree[x]
    return x


def union(x, y):
    tree[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        edge.append((s, e, w))

    ans = 0
    cnt = 0
    tree = [i for i in range(V + 1)]
    edge.sort(key=lambda x: x[2])
    for s, e, w in edge:
        if find_set(s) != find_set(e):
            union(s, e)
            cnt += 1
            ans += w
            if cnt == V:
                break

    print(f'#{tc} {ans}')