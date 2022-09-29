def find_set(x):
    if x != tree[x]:
        tree[x] = find_set(tree[x])
    return tree[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x < y:
        tree[y] = x
    else:
        tree[x] = y


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        edge.append((s, e, w))

    ans = 0
    tree = [i for i in range(V + 1)]
    edge.sort(key=lambda x: x[2])
    for s, e, w in edge:
        if find_set(s) != find_set(e):
            union(s, e)
            ans += w

    print(f'#{tc} {ans}')