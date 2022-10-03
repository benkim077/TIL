# 순열과 조합

[참고 : 순열 및 조합 알고리즘](https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations)

## 순열

- 서로 다른 것 중 몇 개를 뽑아서 한 줄로 나열하는 것

- nPr = n * (n - 1) * ... * (n - r + 1)

- nPn = n!

### 기본적인 순열 생성

```python
for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            for k in range(1, 4):
                if k != i and k != j:
                    print(i, j, k)
```

- 알고 있어야 함!

### 재귀 호출을 통한 순열 생성

#### 1 최소한의 변경(Minimum-change requirement)를 통한 방법

- 각 순열들은 이전의 상태에서 단지 두 개의 요소들 교환을 통해 생성

```python
def f(i, k):
    if i == k:      # 종료
        print(p)        # 해야 할 작성
    else:           # 순열 만들기
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i + 1, k)
            p[i], p[j] = p[j], p[i]

p = [1, 2, 3]
f(0, 3)
```

- 사전 순으로 생성되지 않음.

#### 2 앞에서 사용한 숫자를 표시하는 방식

```python
def f(i, k):
    if i == k:      # 종료
        print(p)        # 해야 할 작업
    else:           # 순열 만들기
        for j in range(k):
            if user[j] == 0:    # a[j]가 아직 사용되지 않았으면
                user[j] = True  # a[j] 사용됨으로 표시
                p[i] = a[j]     # p[i]는 a[j]로 결정
                f(i + 1, k)     # p[i + 1] 값을 결정하러 이동
                user[j] = False # a[j]를 다른 자리에서 쓸 수 있도록 해제

N = 3
a = [i for i in range(1, N + 1)]
p = [0] * N
user = [False] * N
f(0, N)
```

- 사전 순으로 생성

#### 3

> n개 중 r개만 고르고 싶다면?

- 좀 더 일반적인 형태

```python
# 위 코드에서 약간만 변경하면 nPr 기본형
def f(i, k, r):
    if i == r:
        print(p)
    else:
        for j in range(k):
            if user[j] == 0:    # a[j]가 아직 사용되지 않았으면
                user[j] = True  # a[j] 사용됨으로 표시
                p[i] = a[j]     # p[i]는 a[j]로 결정
                f(i + 1, k, r)     # p[i + 1] 값을 결정하러 이동
                user[j] = False # a[j]를 다른 자리에서 쓸 수 있도록 해제

N = 5
R = 3
a = [i for i in range(1, N + 1)]    # 나열할 숫자들을 넣은 리스트
p = [0] * R
user = [False] * N
f(0, N, R)
```

## 조합

- 서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것을 조합(combination)이라고 부른다.

- `nCr = n! / ((n - r)! * r !)`

- `nCr = n-1Cr-1 + n-1Cr` 재귀적 표현

- `nC0 ==  1`

### 재귀 호출을 이용한 조합 생성 알고리즘

```python
def comb(n, r):
    if r == 0:
        print(arr)
    else:
        if n < r:
            return
        else:
            temp[r - 1] = arr[n - 1]
            comb(n - 1, r - 1)
            comb(n - 1, r)
            arr[n - 1] = temp[r - 1]
```

### 10개 중 3개를 고르는 조합

```python
N = 10
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            print(i, j, k)
```

### n 개에서 r개를 고르는 조합(재귀)

```python
def n_combinations_r(n, r, s):  # n개에서 r개를 고르는 조합, s는 선택할 수 있는 구간의 시작
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n - r + 1):
            comb[r - 1] = A[i]
            n_combinations_r(n, r - 1, i + 1)

A = [1, 2, 3, 4, 5]
n = len(A)
r = 3
comb = [0] * r
n_combinations_r(n, r, 0)
```