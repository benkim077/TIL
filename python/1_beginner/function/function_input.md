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

varName을 통해, 특정 argument를 전달

```python
def add(x,y):
  return x + y

add(x = 2, y = 5)
add(2, y = 5)
add(x = 2, 5) # Error. keyword argument 다음에 positional argument 활용할 수 없음
```

### Default Arguments Values

parameter의 기본값 지정해서 argument가 없어도 가능하게 함.

```python
def add (x, y = 0): # 기본값 지정
  return x + y

add(2) # 2
```

## 정해지지 않은 여러 개의 Arguments 처리

'print() 함수는 왜 여러 개 인자를 넣어도 될까?'

정해지지 않은 여러 개의 argument를 처리하기 위해서 Asterisk(*)를 사용한다. 

### Arbitrary Arguments 가변 인자

**몇 개의 argument를 받을지 모르는 함수를 정의할 때**, ***args**를 사용한다.

**여러 개의 argument를 parameter 하나**로 받아서 사용.
**args는 iterable**이다.(리스트 또는 튜플)

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

언패킹시 ***variable**을 사용하면, **남은 요소를 리스트에** 담아준다.

```python
numbers = (1, 2, 3, 4, 5) # 패킹

a, b, *rest = numbers # 1, 2를 제외한 나머지를 rest에 대입
print(a, b, rest) # 1 2 [3, 4, 5]

a, *rest, e = numbers # 1, 5를 제외한 나머지를 rest에 대입
print(rest) # [2, 3, 4]
```

### AsterisK와 *args(가변인자)

```python
def func(*args): # 변경가능한 parameter
  print(args)
  print(type(args)) 

func(1, 2, 3, 'a', 'b') 
# (1, 2, 3, 'a', 'b')
# <class 'tuple'>
```

**\*args는 튜플, \*variable은 리스트**

### Arbitrary Keyword Arguments 가변 키워드 인자(**kwargs)

몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때

**kwargs는 딕셔너리로 묶여 처리

```python
def family(**kwargs):
  for key, value in kwargs.items():
    print(key, ':', value)

family(father= '아부지', mother= '어무니', baby = '아기')
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
```