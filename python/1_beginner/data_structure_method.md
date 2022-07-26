# 데이터 구조 활용

method를 활용

메서드는 클래스 내부에 정의한 함수(객체의 기능)

`data_structure.method()` 형태로 활용

`.`는 dot operator 점 연산자.

## String Type

str은 immutable

변경된 문자열을 새롭게 만들어서 반환

### 문자열 조회/탐색

- `s.find(x)` x의 첫 번째 위치를 반환. 없으면 -1 반환

- `s.index(x)` x의 첫 번째 위치를 반환. 없으면, 오류

### 문자열 검증 메서드

- `s.isalpha()` 알파벳 문자 여부(유니코드 상 Letter, 한국어 포함)

- `s.isupper()` 대문자 여부

- `s.islower()` 소문자 여부

- `s.istitle()` 타이틀 형식 여부

- `s.isdecimal()` 숫자? `s.isdigit()` 소수까지? `s.isnumeric()` 특이한 것들까지

### 문자열 변경 메서드

- `s.replace(old, new[,count])` 바꿀 대상 글자를 새로운 글자로 바꿔서 반환

- `s.strip([chars])` 공백이나 특정 문자 제거

- `s.split(sep=None, maxsplit=-1)` 공백이나 특정 문자를 기준(sep)으로 분리, 리스트로 반환

- `'seperator'.join([iterable])` 구분자로 iterable을 합쳐 문자열 반환

- `s.capitalize()` 가장 첫 번째 글자를 대문자로 바꿈

- `s.title()` 띄어쓰기 기준으로 각 단어 첫글자는 대문자, 나머지는 소문자로 변환

- `s.upper()` 모두 대문자로 변경

- `s.lower()` 모두 소문자로 변경

- `s.swapcase()` 대소문자 서로 변경

## List Type

### 값 추가 및 삭제

- `.append(x)` 마지막에 x 추가

- `.insert(i, x)` idx i에 x삽입

- `.extend(iterable)` iterable의 항목들을 리스트 끝에 추가(+=와 비슷함)

- `.remove(x)` 첫 번째 x 제거, 존재하지 않으면 ValueError

- `.pop(i)` 가장 오른쪽(마지막) 또는 idx i에 있는 항목을 반환하고 제거

- `.clear()` 모든 항목 삭제

### 탐색 및 정렬

- `.index(x[, start, end])` 리스트에 있는 항목 중 가장 왼쪽에 있는 x의 인덱스를 반환

- `.count(x)` x가 몇 개 존재하는지 갯수 반환

```python
# list에서 원하는 값을 모두 삭제하는 방법
my_list = [1, 1, 2, 1, 2, 3, 1, 2, 3, 4]
delete_value = 1

for _ in range(my_list.count(delete_value)):
    my_list.remove(delete_value)

print(my_list) # [2, 2, 3, 2, 3, 4]
```

- `.sort(x)`, `sorted(list)` 리스트를 정렬

    - `.sort([reverser=True | False, key=myFunc])` 원본 리스트 정렬, None 반환

    - `sorted(list)` 정렬된 리스트 반환, 원본 변경 없음

- `.reverse()` 순서를 반대로(정렬 아님), None 반환

## Tuple Type

- immutable. 값에 영향을 미치지 않는 메서드만 지원

- 그 외 메서드는 list와 대부분 동일

- `.index(x)`

- `.count(x)`

## Set

### 추가 및 변경

- `.copy()` set의 얕은 복사본을 반환

- `.add(x)` set에 없다면 x 추가

- `.update(*others)` 

    - 여러 값을 추가

    - others에 있는 모든 항목 중 set에 없는 항목을 추가

### 요소 삭제

- `.remove(x)` x를 set에서 삭제. 없으면 KeyError

- `.discard(x)` x를 set에서 삭제. 에러X

- `.pop()` 임의의 원소 반환, 제거. 비어있으면 KeyError

- `.clear()` 모든 항목 제거

### 집합

- `s.isdisjoint(t)` s가 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True 반환(서로소)

- `s.issubset(t)` s가 t의 하위 셋인 경우, True 반환

- `s.issuperset(t)` s가 t의 상위 셋인 경우, True 반환

## Dictionary

clear(), copy(), keys(), values(), items()

### 조회

> 아래 두 방법 중 어떤 것을 선택할까?

- `.get(key[,default])` key의 값을 반환하는데, 없을 경우 None을 반환

- `my_dict[key]` 없으면 KeyError

- `.setdefault(key[, default])` get과 비슷하다.

    - key가 있으면, value를 리턴

    - key가 없을 경우, default값을 갖는 key를 삽입하고, default를 리턴. default가 없을 경우 value와 리턴은 None이다.

### 추가 및 삭제

- `.pop(key[,default])` key의 값을 반환, 삭제. 없을 경우 default 반환. default 없으면 KeyError

- `.update(other)` 

    - other는 다른 dict나 key-value 쌍으로 되어 있는 모든 iterable.

    - key: value에 덮어쓰기. dictionary의 값을 매핑하며 업데이트 

    - keyword argument 사용

```python
FAANG = {
    'F': 'Facebook',
    # 'A1': 'Apple', # 입력 누락
    # 'A2': 'Amazon',
    'N': 'NEXON', # 잘못 입력했어요!
    'G': 'Google',
}

FAANG.update(N = 'Netflix') # value update 하기

print(FAANG) # {'F': 'Facebook', 'N': 'Netflix', 'G': 'Google'}

AA = {
    'A1': 'Apple',
    'A2': 'Amazon',
}

FAANG.update(AA) # iterable 추가하기

print(FAANG) # {'F': 'Facebook', 'N': 'Netflix', 'G': 'Google', 'A1': 'Apple', 'A2': 'Amazon'}

```
