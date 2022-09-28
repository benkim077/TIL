def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


V, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([u, v, w])
edge.sort(key=lambda x:x[2])
rep = [i for i in range(V + 1)]

N = V + 1   # 실제 정점 수
cnt = 0     # 선택한 edge 수
total = 0   # MST 가중치의 합
for u, v, w in edge:
    if find_set(u) != find_set(v):
        cnt += 1
        union(u, v)
        total += w
        if cnt == N - 1:
            break

print(total)