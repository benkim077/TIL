# dfs

## 스택

### 스택의 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조

- 선형구조 : 자료 간의 관계가 1대1의 관계를 갖는다.

    - 비선형구조 : 자료 간의 관계가 1대N의 관계를 갖는다.(트리)

- 마지막에 삽입한 자료를 가장 먼저 꺼낸다

    - 후입선출(LIFO, Last-In-First-Out)

### 스택의 구현

- 배열, 리스트를 사용

- 마지막 삽입 위치 top

- push, pop, isEmpty, peek

## dfs

### 반복으로 dfs 구현(stack)

지나간 정점을 저장하는 방법

#### 갈림길을 저장하는 방법

```python
# 기본 코드
stk = []
def dfs(v):
    stk.append(v)
    while stk:
        v = stk.pop()
        if not vsted[v]:
            vsted[v] = True
            for w in adj_lst[v]:
                if not vsted[w]:
                    stk.append(w)
```

- 스택으로 dfs를 구현하는 기본 코드

```python
# 수정 코드
stk = []
def dfs(v):
    stk.append(v)
    vsted[v] = True
    while stk:
        v = stk.pop()
        print(v)
        for w in adj_lst[v]:
            if not vsted[w]:
                stk.append(w)
                vsted[w] = True
```

- 스택에 넣을 때 vsted를 체크하는 방식으로 수정한 코드

- 스택에 들어간 적이 없으면 푸시해

- 스택에 들어가 있다면, 또 넣지마

- 중복해서 들어가지 않기 때문에 스택의 크기를 정할 수 있다. 정점의 갯수만큼만 만들면 된다.

- bfs와 비슷한 구조로 사용할 수 있게 된다.

- dfs를 하는데 순회 방법에 대한 조건이 있으면, 기본 코드를 사용하고, 그냥 빠짐없이 돌면 되는 경우에는 수정된 코드를 사용하면 된다.

- 반복구조의 dfs를 사용할 때 수정 코드를 사용한다.