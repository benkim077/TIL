# 변수 Variable

- **‘데이터 저장 → 처리’가 프로그래밍의 핵심**

- 변수는 **데이터 1개를 저장할 수 있는 자료구조**
- 데이터 저장
- 변수를 사용하면 복잡한 값들을 쉽게 사용할 수 있음(**추상화**)

## 변수의 할당 assignment

- 할당 연산자 (=)
- 각 변수의 값을 바꿔서 저장하기

```python
# pythonic
x = 10
y = 20
x, y = y, x
print(x, y) # => 20 10
```

## 식별자 identifier
변수 이름 규칙

- 식별자 이름은 **영문 알파벳 _ 숫자**
- 첫 글자에 숫자 X
- 대소문자 구별
- keyword는 예약어. 식별자 이름으로 사용할 수 없음(keyword.kwlist)

```python
import keyword
print(keyword.kwlist)
```

- 내장 함수나 모듈 등도 사용하지 말아야 한다.

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

값이 없음
일반적으로 반환 값이 없는 함수에서 사용

## Boolean Type

- 논리 자료형. 참 거짓 표현
- True, False
- 비교 / 논리 연산에서 활용

### 비교 연산자

- == 같음
- != 같지 않음
- is 객체 아이덴티티(OOP)
- is not 객체 아이덴티티가 아닌 경우

### 논리 연산자

- A and B  모두 True → True
- A or B  모두 False → False
- Not  True → False, False → True
- 우선순위 not > and > or

```python
print(not True and False or not False) # True
```

### Truthy False

False는 아니지만, False로 취급되는 다양한 값

- 0
- 0.0
- ()
- []
- {}
- None
- ''(빈 문자열)

### 논리 연산자의 단축 평가

- 결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째 값 반환
    - and  첫 값이 False인 경우 무조건 False ⇒ 첫번째 값 반환
    - or 첫 값이 True인 경우 무조건 True ⇒ 첫번째 값 반환

```python
# 평가가 끝나는 평가식의 값이 리턴
# and 
print(3 and 5) # 5 
print(3 and 0) # 0 
print(0 and 3) # 0 단축 평가
print(0 and 0) # 0 단축 평가
# or
print(5 or 3) # 5 단축 평가
print(3 or 0) # 3 단축 평가
print(0 or 3) # 3 
print(0 or 0) # 0 
```

# 컨테이너 Container

데이터를 여러 개 저장하는 객체
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

- 순서가 있다. 0번째 부터
- 생성
    - [] 또는 list()
    - 어떤 자료형도 저장 가능
    - 내용 변경 가능
- 접근
    - 인덱스
    - list[i] (i == 0, 1, 2, ...)

## 튜플 Tuple Type

- 리스트와 동일하지만, 내용 변경 불가능(immutable)한 시퀀스
- 생성 및 접근
    - () 또는 tuple()
    - 인덱스로 접근 가능 tuple[i]
- 주의사항
    - 단일 항목 튜플 (1,) (반드시 뒤에 ,)
    - 복수 항목 튜플 (1, 2, 3,) (, 권장)

### 튜플 대입
```python
x, y = 1, 2 # 실제로 x, y = (1, 2) 로 처리된다.
```

## Range Type

숫자의 시퀀스를 나타내기 위해 사용

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

```python
print([1, 2, 3, 5][1:4]) # [2, 3, 5]

print((1, 2, 3)[:2]) # (1, 2)

print(range(10)[5:8]) # range(5, 8)

print('abcd'[2:4]) # cd
```

간격 슬라이싱

```python
print([1, 2, 3, 5][0:4:2]) # [1, 3]
```

문자열 슬라이싱

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

### Set 생성

- {} 또는 set()
- 빈 set를 만들 땐, 반드시 set() 사용
    - type({})는 dict

### Set 활용

- 다른 컨테이너의 중복된 값을 쉽게 제거
- 단, 순서가 없어진다.

### Set 집합 연산

- |  합집합
- &  교집합
- \-  차집합
- ^ 대칭차집합

## Dictionary Type 딕셔너리

- key - value 쌍으로 이뤄진 자료형
- 3.7v 부터 ordered

### Key

- 변경 불가능한 데이터(immutable)만 활용 가능
- string, integer, float, boolean, tuple, range

### Value

- 모든 type 사용 가능

### 생성 및 접근

- {} 혹은 dict()
- key를 통해 value에 접근

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

# 파이썬 프로그램 구성 단위

- 식별자
    - 변수, 함수, 클래스 등 다양한 값을 가질 수 있는 이름
    - 예약어
- 리터럴(literal)
    - 읽혀지는 대로 쓰여있는 **값** 그 자체
- 표현식(Expression)
    - 새로운 데이터 값을 생성하거나 계산하는 코드 조각
- 문장(Statement)
    - 특정한 작업을 수행하는 코드 전체
    - 파이썬이 실행 가능한 최소한의 코드 단위

> 모든 표현식은 문장이다.