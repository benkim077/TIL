# 분할 정복

- 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눈다.

- 정복(Conquer) : 나눈 작은 문제를 각각 해결한다.

- 통합(Combine) : (필요하다면) 해결된 해답을 모은다.

> Top-down Approach

## 병합 정렬

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

- 분할 정복 알고리즘 활용

    - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄

    - top-down 방식

- 시간복잡도 O(n log n)

### 분할 단계

- 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속한다.

```python
def merge_sort(lst):
    if len(lst) == 1:
        return lst

    m = len(lst) // 2
    left = merge_sort(lst[:m])
    right = merge_sort(lst[m:])

    return merge(left, right)
```

### 병합 단계

- 2개의 부분집합을 정렬하면서 하나의 집합으로 병합

- 하나로 병합될 때까지 반복

```python
def merge(left, right):
    lst = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                lst.append(left.pop(0))
            else:
                lst.append(right.pop(0))
        elif len(left) > 0:
            lst.append(left.pop(0))
        elif len(right) > 0:
            lst.append(right.pop(0))

    return lst
```

## 퀵 정렬

- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.

- 다른 점 1

    - 병합 정렬은 그냥 두 부분으로 나누는 반면에, 퀵 정렬은 분할할 떄, 기준 아이템(pivot item) 중심으로, 이 보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.

- 다른 점 2

    - 각 부분 정렬이 끝난 후, 병합정렬은 '병합'이란 후처리 작업이 필요, 퀵 정렬은 필요 없음.

### 피봇을 정하는 방법

- 퀵 정렬은 피봇을 어떻게 정하느냐가 성능을 정하는 관건

#### Hoare-Partition 알고리즘

- P(피봇)값들 보다 큰 값은 오른쪽, 작은 값들은 왼쪽 집합에 위치하도록 한다.

- 피봇을 두 집합의 가운데에 위치시킨다.

```python
def partition(l, r):
    pivot = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def qsort(l, r):
    if l < r:
        s = partition(l, r)
        qsort(l, s - 1)
        qsort(s + 1, r)

A = [7, 2, 5, 3, 4, 5]
N = len(A)
qsort(0, N - 1)
print(A)
```

- 맨 왼쪽부터 시작해서 피봇을 구하는 경우

- `[[4, 5], [2, 3], [2, 1], [1, 0]]`을 1번 인덱스를 기준으로 비교하고 싶다면?

    - 파티션 함수 내부에 비교하는 부분만 새로운 함수를 넣어서 구현

#### Lomuto Partition 알고리즘



#### 퀵 정렬 코드

```python
def qsort(lst, s, e):
    if s >= e:
        return lst
    
    key = s
    i, j = s + 1, e

    while i <= j:
        while i <= e and lst[i] <= lst[key]:
            i += 1
        while j > s and lst[j] >= lst[key]:
            j -= 1
        if i > j:
            lst[j], lst[key] = lst[key], lst[j]
        else:
            lst[i], lst[j] = lst[j], lst[i]
    
    qsort(lst, s, j - 1)
    qsort(lst, j + 1, e)
```

## 이진 검색

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

    - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행

- **이진 검색을 하기 위해서는 자료가 정렬된 상태**여야 한다.

### 검색 과정

1. 자료의 중앙에 있는 원소를 고른다.

2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.

3. 목표 값이 중앙 원소의 값보다 작으면 자료의 원쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.

4. 찾고자 하는 값을 찾을 때까지 1~3을 반복

### 반복 구조로 구현

```python
def bin_search(target, lst, s, e):     # target, lst, start, end
    while s <= e:
        m = (s + e) // 2
        if lst[m] == target:    # 찾았다!
            return 1
        elif lst[m] < target:   # 오른쪽에 있는 경우
            s = m + 1
        else:                   # 왼쪽에 있는 경우
            e = m - 1
    return 0                # 못 찾은 경우
```

### 재귀 구조로 구현

```python
def bin_search(lst, s, e, key):
    if s > e:
        return -1
    else:
        m = (s + e) // 2
        if key == lst[m]:
            return m
        elif key < lst[m]:
            return bin_search(lst, s, m - 1, key)
        else:
            return bin_search(lst, m + 1, e, key)
```

- 반복구조로 쉽게 짤 수 있으므로, 굳이 재귀를 사용할 필요는 없다.

## 분할 정복의 활용

- 병합 정렬은 외부 정렬의 기본이 되는 정렬 알고리즘이다. 또한 멀티코어 CPU나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용된다. 

- 퀵 정렬은 매우 큰 입력 데이터에 대해서 좋은 성능을 보이는 알고리즘이다.