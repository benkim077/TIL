# 문자열

## 패턴 매칭 알고리즘

### 고지식한 패턴 검색 알고리즘

- Brute Force

### 카프-라빈 알고리즘

- 맞은 만큼만 shift해서 거기서부터 비교 시작

    - abcd에서 abc까지 맞았으면, 3칸 shift하고, d부터 시작

- 틀린 지점에 따라 어디로 돌아갈지 미리 계산한다. (패턴을 사용)

    - 룩 업 테이블을 활용

```python
# 룩 업 테이블 활용 예시
# 가위 바위 보를 할 때 결과를 출력하는 프로그램
# if, else를 사용하지 말고 룩 업 테이블을 활용하면
# 메모리 공간 더 활용하지만, 실행 속도를 상당히 개선할 수 있다.
# 나와 cpu의 승/패 결과를 적어둔 룩 업 테이블을 만들면 된다.
```

### KMP 알고리즘

### 보이어-무어 알고리즘

- 오른쪽에서 왼쪽으로 비교

- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘

- 끝을 먼저 비교하는 것

- 패턴을 분석해서 항상 길이 만큼 이동하지 않도록 함

    - 룩 업 테이블

## 문자열 암호화

### exclusive-or

- 0과 XOR을 하면, 원래 값이 나오고

- 1과 XOR을 하면, 반대 값이 나온다.

- 받은 암호를 키와 XOR 연산하면, 원래 평문을 알 수 있다.

### 문자열이 있을 때, 저장소의 크기를 줄이며 정확한 정보를 저장하는 방법?

- Run-length encoding 알고리즘

    - 같은 값이 몇 번 반복되는가를 나타냄으로 압축

- 이외에도 변화값을 저자아는 방식으로 데이터를 압축하는 방식이 있다.

## 참고 코드

- 문자열 패턴 매칭 알고리즘(KMP)

### 첫 번째

```python
N = len(t)
M = len(p)
lps = [0] * (M+1)
# preprocessing
j = 0 # 일치한 개수== 비교할 패턴 위치
lps[0] = -1
for i in range(1, M):
    lps[i] = j          # p[i]이전에 일치한 개수
    if p[i] == p[j]:
        j += 1
    else:
        j = 0
lps[M] = j
# search
i = 0   # 비교할 텍스트 위치
j = 0   # 비교할 패턴 위치
while i < N and j <= M:
    if j==-1 or t[i]== p[j]:     # 첫글자자 불일치했거나, 일치하면
        i += 1
        j += 1
    else:               # 불일치
        j = lps[j]
    if j==M:    # 패턴을 찾을 경우
        print(i-M, end = ' ')    # 패턴의 인덱스 출력
        j = lps[j]

print()
return


t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)
t = 'AABAACAADAABAABA'
p = 'AABA'
kmp(t, p)
t = "AAAAABAAABA"
p =  "AAAA"
kmp(t, p)
t = "AAAAABAAABA"
p =  "AA"
kmp(t, p)
```

### 두 번째

```python
M = len(pat)
N = len(txt)

# create lps[] that will hold the longest prefix suffix 
# values for pattern
lps = [0]*M
j = 0 # index for pat[]

# Preprocess the pattern (calculate lps[] array)
computeLPSArray(pat, M, lps)

i = 0 # index for txt[]
while i < N:
    if pat[j] == txt[i]:
        i += 1
        j += 1

    if j == M:
        print ("Found pattern at index " + str(i-j))
        j = lps[j-1]

    # mismatch after j matches
    elif i < N and pat[j] != txt[i]:
        # Do not match lps[0..lps[j-1]] characters,
        # they will match anyway
        if j != 0:
            j = lps[j-1]
        else:
            i += 1
  
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)
```