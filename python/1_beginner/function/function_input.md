# Function Input

함수 입력

## Parameter, Argument

- parameter
  - 함수 선언할 때, 함수 내부에서 사용되는 변수
  - 매개변수
- argument
  - 함수 호출할 때, 넣어주는 값
  - 인자

### Argument

호출 시 함수의 parameter로 전달

- 필수 argument : 없으면 에러
- 선택 argument : 값을 전달하지 않아도 되는 경우는 기본값 전달

### Positional Arguments

argument의 순서 == parameter의 순서

기본 규칙이다.

### Keyword Arguments

직접 변수의 이름으로 특정 argument를 전달할 수 있음

keyword argument 다음에 positional argument 활용할 수 없음

```python
def add(x,y):
  return x + y

add(x = 2, y = 5)
add(2, y = 5)
add(x = 2, 5) # Error. 
```

### Default Arguments Values

parameter의 기본값 지정해서 argument가 없어도 가능하게 함.

```python
def add (x, y = 0): # 기본값 지정
  return x + y

add(2) # 2
```

## 정해지지 않은 여러 개의 Arguments 처리

print() 함수는 왜 여러 개 인자를 넣어도 될까?

정해지지 않은 여러 개의 argument를 처리하기 위해서 Asterisk(*)를 사용한다. 

### 가변 인자(*args)

여러 개의 Positional argument를 하나의 필수 parameter로 받아서 사용

언제 사용?

- 몇 개의 positional argument를 받을지 모르는 함수를 정의할 때 유용

```python

```

### 패킹 / 언패킹

패킹

- 여러 개의 데이터를 묶어서 변수에 할당하는 것

`numbers = (1, 2, 3, 4, 5)`

언패킹

- 시퀀스의 요소들을 여러 변수에 나누어 할당하는 것

`a, b, c, d, e = numbers`

언패킹시 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야 함

```python
numbers = (1, 2, 3, 4, 5) # 패킹
a, b, c, d, e, f = numbers # 언패킹
# ValueError
```

언패킹시 왼쪽의 변수에 asterisk(*)를 붙이면, 할당하고 남은 요소를 리스트에 담을 수 있음

```python
numbers = (1, 2, 3, 4, 5) # 패킹

a, b, *rest = numbers # 1, 2를 제외한 나머지를 rest에 대입
print(a, b, rest) # 1 2 [3, 4, 5]

a, *rest, e = numbers # 1, 5를 제외한 나머지를 rest에 대입
print(rest) # [2, 3, 4]
```

### AsterisK(*)와 가변 인자

```python
def func(*args): # 변경가능한 parameter
  print(args)
  print(type(args)) 

func(1, 2, 3, 'a', 'b') 
# (1, 2, 3, 'a', 'b')
# <class 'tuple'>
```

**함수 안에선 튜플로, 그냥 쓸 때는 리스트로**

### 가변 키워드 인자(**kwargs)

키워드 인자는 유도탄

가변 키워드 인자는 키워드 인자가 여러 개

몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용

**kwargs는 딕셔너리로 묶여 처리

```python
def family(**kwargs):
  for key, value in kwargs.items():
    print(key, ':', value)

family(father= '아부지', mother= '어무니', baby = '아기')
```

```python
def print_family_name(father, mother, **pets):
  print('아버지 :', father)
  print('어머니 :', mother)
  if pets: # pets에 값이 없다면 [], {} => falsy
    print('반려동물들..')
    for species, name in pets.item():
      print(f'{species} : {name}')

print_family_name('아부지', '어무이', dog = '멍멍이', cat = '냥냥이')

# 아버지 : 아부지
# 어머지 : 어무이
# 반려동물들..
# dog : 멍멍이
# cat : 냥냥이
```

### 가변 인자와 가변 키워드 인자 동시 사용 예시

```python
def print_family_name(*parents, **pets):
  print('아버지 :', parents[0])
  print('어머니 :', parents[1])
  if pets:
    print("반려동물들..")
    for title, name in pet.items():
      print(f'{} : {}'.format(title, name))

print_family_name('아부지', '어무이', dog = '멍멍이', cat = '냥냥이')