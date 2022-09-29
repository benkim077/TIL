INF = 10000


def dijkstra(start):
    distance[start] = 0
    vsted[start] = 1
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(N - 1):
        now = get_smallest_node()
        vsted[now] = 1

        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost


def get_smallest_node():
    min_v = INF
    min_i = 0
    for i in range(1, N + 1):
        if distance[i] < min_v and not vsted[i]:
            min_v = distance[i]
            min_i = i
    return min_i


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())

    graph = [[] for i in range(N + 1)]  # 각 노드에 연결된 노드에 대한 정보
    vsted = [0] * (N + 1)               # 방문 체크
    distance = [INF] * (N + 1)          # 최단 거리

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    dijkstra(0)

    print(f'#{tc} {distance[N]}')
