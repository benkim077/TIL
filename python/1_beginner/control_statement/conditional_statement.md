# Conditional Statement

조건의 True, False 에 따라, 프로그램의 분기를 나눠 실행한다.

## if, else, elif

### 기본 문법

```python
if condition1:
  # condition1 == True 일 때 실행
elif condition2:
  # condition2 == True 일 때 실행
else:
  # others 나머지
```

### 조건문 중첩

```python
# id, pw 확인하는 예시
if inputId == USERNAME:
  if inputPw == PASSWORD:
    print('로그인 되었습니다.')
  else:
    print('비밀번호를 확인해주세요.')
else:
  print('id를 확인해주세요.')
```

## Conditional Expression 

**조건 표현식**(**삼항 연산자**)은 조건문을 표현식의 형태로 바꾼 것

### Expression

**표현식**이란 어떤 **값으로 평가**되는 구절이다.
```python
a, b = 5, 4
# 아래 문장들이 어떻게 평가되는지 확인해보자.
a # 5
a == 5 # True
a + b + 3 # 12
```

### Syntax

조건 표현식은 **condition에 따라 분기되는 값**을 이용한다.
이 값이 **조건 표현식의 평가값**이다.

```python
# condition == True이면 trueValue가,
# condition == False이면 FalseValue가 조건 표현식의 평가값이다.
trueValue if condition else FalseValue # trueValue 또는 FalseValue로 평가
```

### Evaluate, How to Use

```python
# 조건 표현식의 평가 및 활용
age = 30
isAdult = '성인' if age >= 20 else '미성년자'
```

## Conditional Statement vs. Conditional Expression

조건문과 삼항 연산자를 어떻게 사용해야할까?

- 삼항연산자는 condition에 따라 평가값이 달라진다.
이 **평가값을 활용하여 코드를 작성하는 경우**(변수에 할당하는 등)는 삼항 연산자를 활용한다. 

- 반면 조건문은 condition에 따라 **특정 코드 블럭을 실행**하는 경우에 사용한다.