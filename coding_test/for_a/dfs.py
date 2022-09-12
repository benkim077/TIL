def dfs(graph, v, vsted):
    # 현재 노드를 방문 처리
    vsted[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not vsted[i]:
            dfs(graph, i, vsted)

# 각 노드가 연결된 정보를 표현(그래프를 2차원 리스트로 나타낼 수 있다.)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5], 
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
vsted = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, vsted) # => 1 2 7 6 8 3 4 5
