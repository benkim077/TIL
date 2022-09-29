def find_set(x):
    while tree[x] != x:
        x = tree[x]
    return x


def union_set(x, y):
    tree[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    tree = [i for i in range(0, N + 1)]
    data = list(map(int, input().split()))

    for i in range(M):
        s, e = data[2 * i], data[2 * i + 1]
        union_set(s, e)

    check = [0] * (N + 1)
    for i in range(1, N + 1):
        check[find_set(i)] = 1

    print(f'#{tc} {sum(check)}')