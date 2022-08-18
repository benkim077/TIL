# DFS 깊이 우선 탐색

- 그래피는 자료가 n:m 관계인 비선형 자료 구조.

- 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요

- 그래프 탐색 방법 두 가지

> 탐색 목적에 따라 선택

    - 깊이 우선 탐색(Depth First Search, DFS)

    - 너비 우선 탐색(Breadth First Search, BFS)

## DFS

- 시작 정점(출발점)의 한 방향으로 갈 수 있는 경로의 끝까지 탐색하고, 가장 마지막에 만났던 갈림길으로 되돌아와, 다른 방향으로 탐색을 반복하여, 결국 모든 정점을 방문하는 순회방법

- 경로를 저장하는 방법 2가지

    - 스택에 저장

    - 재귀 호출로 호출 단계 함수 안에 저장

- 구조 스택 자료 구조 사용

    - 순회 중 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로, 

### 스택으로 DFS 구현

1. 시작 정점 v를 결정하여 방문

2. v의 인접한 점 중에서

    - 방문하지 않은 w가 있으면, v를 스택에 push하고 w 방문.

        - w를 v로 하여 다시 2. 를 반복

    - 방문하지 않은 정점이 없으면, 스택을 pop하여 
    
        - 받은 가장 마지막 방문 정점을 v로 하여 2. 반복

3. 스택이 공백이 될 때까지 2. 반복

### 구현

- 인접 배열 만들기

- visited[], stack[]을 사용