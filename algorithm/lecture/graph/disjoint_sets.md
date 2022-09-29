# 서로소 집합

- 서로소 집합 자료구조

- 서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합들이다.(교집합이 없다.)

- 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다. 이를 대표자(representative)라 한다.

- 상호배타 집합을 표현하는 방법

    - 연결 리스트

    - 트리

- 상호배타 집합 연산

    - Make-Set(x) : x가 대표원소인 집합을 만든다.

    - Find-Set(x) : x가 속해있는 집합의 **대표원소를 출력**

    - Union(x, y) : x가 대표원소인 집합과, y가 대표원소인 집합을 합침(앞에 있는 x를 대표원소로 함)

        - x의 대표원소를 찾고(find-set(x))

        - y의 대표원소를 찾고(find-set(y))

        - y의 대표원소를 x의 대표원소로 교체

## 상호배타 집합 표현 - 트리

- 하나의 집합을 하나의 트리로 표현

- 자식 노드가 부모 노드를 가리키며 루트 노드가 대표자가 된다.

- 대표 원소는 자신을 가리킨다.

### 연산

- 트리 갯수 구하기

    - 인덱스가 자기 자기 자신과 같은 정점의 갯수가 트리의 갯수가 된다.

- Make-Set(x) : 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산

```
Make-Set(x)
    p[x] = x
```

- Find-Set(x) : x를 포함하는 집합을 찾는 연산(**대표원소 찾기**)

    - 인덱스와 자기 자신이 다르면

    - 계속 찾아간다.

```
# 반복 구조
Find-Set(x)
    WHILE P[x] != x:    // x == p[x]는 대표 원소(루트)에 도착했다는 뜻.
        x = p[x]
    RETURN x
```

```
# 재귀 구조
Find-Set(x)
    IF x == p[x] : RETURN x
    ELSE : RETURN Find-Set(p[x])
```

- Union(a, b)

    - r1 = findset(a)

    - r2 = findset(b)

    - tree[r2] = r1

```
Union(x, y)
    p[Find-Set(y)] = Find-Set(x)
```

#### 연산의 효율을 높이는 방법

- Rank를 이용한 Union

    - 각 노드는 자신을 루트로 하는 subtree의 높이를 Rank라는 이름으로 저장

    - 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙인다

- Path compression

    - Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어준다

#### 연산 효율 높이는 방법들의 코드

```
Make_Set() 연산

p[x] : 노드x의 부모 저장
rank[x] : 부모 노드가 x인 트리의 랭크 값 저장

Make_Set(x)
    p[x] = x
    rank[x] = 0
```

```
Find_Set(x) 연산

#1 방법
Find_Set(x)
    IF x != p[x]    // x가 루트가 아닌 경우
        p[x] = Find_set(p[x])
    RETURN p[x]

#2 방법
Find_Set(x)
    IF x == p[x]
        RETURN x
    p[n] = Find_Set(p[n])
    RETURN p[n]
```

- 특정 노드에서 루트까지 경로를 **찾아가면서 노드의 부모 정보를 갱신**

- **경로 압축 기법**

```
Union(x, y) 연산

Union(x, y)
    Link(Find_Set(x), Find_Set(y))

Link(x, y)
    IF rank[x] > rank[y]
        p[y] = x
    ELSE
        p[x] = y
        IF rank[x] == rank[y]
            rank[y]++
```



