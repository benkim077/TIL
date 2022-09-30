# 최단 경로

- 최단 경로 정의

    - 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로

- 하나의 시작 정점에서 끝 정점까지의 최단 경로

    - 다익스트라(dijkstra) 알고리즘

        - 음의 가중치를 허용하지 않음

    - 벨만-포드(Bellman-Ford) 알고리즘

        - 음의 가중치 허용

- 모든 정점들에 대한 최단 경로

    - 플로이드-워샬(Floyd-Warshall) 알고리즘

## Dijkstra 알고리즘

- 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식

- 시작 정점(s)에서 끝 정점(t)까지의 최단 경로에 정점 x가 존재한다.

- 이때, 최단경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단경로로 구성된다.

- 탐욕 기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사하다.

```
s: 시작 정점, A: 인접 행렬, D: 거리, V: 정점 집합, U: 선택된 정점 집합
Dijkstra(s, A, D)
    U = {s}             # U: 비용이 결정된 정점의 집합

    FOR 모든 정점 v
        D[v] = A[s][v]  # D[v] : 시작점s에서 v에 도착하는 최소비용을 저장

    WHILE U != V        # 아직 선택되지 않은 정점이 남아있으면
        D[w]가 최소인 정점 w (아직 U에 포함되지 않은 녀석들 중에서) 선택
        U = U 합집합 {w}

        FOR w에 인접한 모든 정점 v
            D[v] = min(D[v], D[w] + A[w][v])    # 기존 비용과 w를 거쳐가는 비용을 비교하고, 새로운 비용으로 갱신
```

```python
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
```