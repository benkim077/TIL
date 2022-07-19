# 자료형 Data Type

- Boolean Type 불린형
- Numeric Type 수치형
    - int 정수
    - float 부동소수점 실수
    - complex 복소수
- String Type 문자열
- None

자료형 검사 함수 type()

## Float Type

부동 소수점 문제 해결 방법
```python
import math
print(math.isclose(a, b))
```

## String Type

### f-string

```python
variable = ben
print(f'Hello, {variable}!') # {}안에 변수를 넣어서 사용
print(f'{variable * 3}') # 간단한 계산도 가능
```

###  문자열 연산
- 덧셈

```python
print('hello' + 'world') # => hello world
```

- 곱셈

```python
print('hello' * 3) # => hellohellohello
```

### String Interpolation
문자열 보간(사이를 연결하는 것)

python 3.6 부터 f-strings 사용
더 빠르고 편리하다.
```python
name = 'Ben'
score = 100
print(f'Hello, {name}! 성적은 {score}') # => Hello, Ben! 성적은 100
```

## None Type

**값이 없음**
일반적으로 반환 값이 없는 함수에서 사용

## Boolean Type

- 논리 자료형. 참 거짓 표현
- True, False (값)
- 비교 / 논리 연산에서 활용

# 컨테이너 Container

**데이터를 여러 개 저장**하는 **객체**
서로 다른 Type 저장 가능

## 분류

Ordered, Unordered로 크게 분류
순서가 있다 != 정렬

- 컨테이너
    - 시퀀스형(ordered)
        - 리스트
        - 튜플
        - 레인지
    - 비시퀀스형(unordered)
        - 세트
        - 딕셔너리

> 시퀀스 시작

## 리스트 List Type

### 선언
- [] 또는 list()
### 순서 
- 순서가 있다. 0번째 부터
### 중복
- 중복 허용
### 접근
- 인덱스
- list[i] (i == 0, 1, 2, ...)
- 파이썬은 음수 인덱스 가능
### 수정, 추가, 삭제
- 수정 가능
- 추가 append(), insert(), extend()
- 삭제 remove(), pop(), clear()

## 튜플 Tuple Type

리스트와 동일하지만, 이후 내용 변경 불가능(immutable).

### 선언
- () 또는 tuple()
### 순서
- 순서 있음
### 중복
- 중복 허용
### 접근
- 인덱스로 접근 가능 tuple[i]
### 수정, 추가, 삭제
- **튜플은 수정, 추가, 삭제가 불가능** 
### 주의사항
- 단일 항목 튜플 (1,) (반드시 뒤에 ,)
- 복수 항목 튜플 (1, 2, 3,) (, 권장)

### 튜플 대입
```python
x, y = 1, 2 # 실제로 x, y = (1, 2) 로 처리된다.
```

## Range Type

숫자의 시퀀스를 나타내기 위해 사용.
range()는 리스트가 아니다. list로 변경하기 위해서 `list(range(5))` 리스트로 묶어준다.

```python
range(0, 4) # [0, 1, 2, 3]
```

### 사용 방법

- 기본
    - range(n)  0부터 n-1까지 숫자 시퀀스
- 범위 지정
    - range(n, m)  n부터 m-1까지 숫자 시퀀스
- 범위 및 스텝
    - range(n, m, s)  n부터 m-1까지 step만큼 증가시키며 숫자 시퀀스

## 시퀀스 슬라이싱 Slicing

시퀀스의 특정 부분만 잘라낼 수 있다.
`list[start, end, step]`

```python
print([1, 2, 3, 5][1:4]) # [2, 3, 5]

print((1, 2, 3)[:2]) # (1, 2)

print(range(10)[5:8]) # range(5, 8)

print('abcd'[2:4]) # cd
```

### 간격 슬라이싱

```python
print([1, 2, 3, 5][0:4:2]) # [1, 3]
```

슬라이싱을 통해 **반복문을 대체**하는 방법

```python
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list = list[::2] # [1, 3, 5, 7, 9]
```

### 문자열 슬라이싱

```python
s = 'abcdefghi'
s[::] # 'abcdefghi'
s[::-1] # 'ihgfedcba'
```

> 비시퀀스 시작

## Set Type 세트

- Set는 집합이다.
- 요소의 중복 없음
- 순서 상관 없음(인덱스로 접근 불가)
- mutable 가변 자료형

### 선언

- {} 또는 set()
- 빈 set를 만들 땐, 반드시 set() 사용
    - type({})는 dict

### 중복

- **중복 허용 X**
- **다른 컨테이너의 중복된 값을 쉽게 제거**
- 단, 순서가 없어진다.

### 접근

- 순서가 없어, index를 이용한 접근 불가

### 수정, 추가, 삭제

- 수정 불가
- 추가 add(), update()
- 삭제 remove(), discard(), pop(), clear()

### Set 집합 연산

- |  합집합
- &  교집합
- \-  차집합
- ^ 대칭차집합

## Dictionary Type 딕셔너리

- key-value 쌍으로 이뤄진 자료형

### Key

- 변경 불가능한 데이터(immutable)만 활용 가능
- string, integer, float, boolean, tuple, range

### Value

- 모든 type 사용 가능

### 선언

- {} 혹은 dict()

### 순서

- 3.7v 부터 ordered

### 중복

- 중복 허용 X

### 접근

- key를 통해 value에 접근

### 수정, 추가, 삭제

- value 수정 가능
- 추가
    - d[key] = val
    - update() 메소드
- 삭제
    - pop(), popitem(), clear() 메소드

```python
# a, b가 같은 내용을 갖는다.
dict_a = {'a': 'apple', 'b': 'banana', 'list': [1, 2, 3]}
print(dict_a)

dict_b = dict(a = 'apple', b = 'banana', list = [1, 2, 3]) # 'a'가 아니라, a
print(dict_b)
```

## Typecasting 형 변환

데이터 형태는 서로 변환할 수 있다.

- 암시적 형 변환(implicit)
- 명시적 형 변환(explicit)

**암시적 형 변환을 의도적으로 사용 X**
**명시적 형 변환만 사용**

### 암시적 형 변환

- 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환하는 경우
- by Python 자동으로

```python
print(True + 3) # 4

print(3 + 5.0) # 8.0
```

### 명시적 형 변환

- 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환하는 경우
- by Developer 의도적으로

```python
print('3' + 4) # TypeError

print(int('3') + 4) # 7

print(int('3.5') + 5) # ValueError 
```

```python
print('3.5' + 3.5) # TypeError

print(float('3')) # 3.0

print(float('3/4') + 5.3) # ValueError
```