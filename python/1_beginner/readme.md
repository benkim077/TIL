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
- 내장 함수나 모듈 등도 사용하지 말아야 한다.

# 자료형 Data Type

- Boolean Type 불린형
- Numeric Type 수치형
    - int 정수
    - float 부동소수점 실수
    - complex 복소수
- String Type 문자열
- None

## 문자열 연산
- 덧셈

```python
print('hello' + 'world') # => hello world
```

- 곱셈

```python
print('hello' * 3) # => hellohellohello
```

## String Interpolation
문자열 보간(사이를 연결하는 것)

python 3.6 부터 f-strings 사용
더 빠르고 편리하다.
```python
name = 'Ben'
score = 100
print(f'Hello, {name}! 성적은 {score}') # => Hello, Ben! 성적은 100
```