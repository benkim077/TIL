# 조합

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
            temp[r - 1] = an[n - 1]
            comb(n - 1, r - 1)
            comb(n - 1, r)
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