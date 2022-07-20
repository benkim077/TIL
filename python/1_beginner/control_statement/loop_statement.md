# 반복문

## while

조건이 참인 경우 반복적으로 코드 실행

## for

iterable object의 element를 모두 순회

### What is iterable?
  - Data Type
    - string, list, dict, tuple, set
  - iterable function
    - range, enumerate

### Syntax

```python
for elementsVariable in iterable:
  # code
```

### Dictionary 순회

- 기본으로 key를 순회, 루프 안에서 `dict[key]`로 value에 접근

```python
# example code

```

#### 메서드 활용 순회

keys(), values()
- list 리턴 
- `dict_keys(['k1', 'k2']` `dict_values([v1, v2])`

items()
- list 안에 튜플 리턴 
- `dict_items([('k1', v1), ('k2', v2)])`

### Enumerate 순회

(idx, value) 튜플로 구성된 열거(enumerate) 객체 반환

#### Syntax

```python
# enumerate(iterable[,start=0])
members = ['a', 'b', 'c']
list(enumerate(members)) # [(0, 'a'), (1, 'b'), (2, 'c')]
```

### List Comprehension

특정 값을 가진 리스트를 생성하는 간결한 코드

#### Syntax

```python
# code가 list element가 된다.
newList1 = [code for variable in iterable]
newList2 = [code for variable in iterable if condition]
```

```python
# ex code

```

### Dictionarary Comprehension

특정 값을 가진 딕셔너리를 생성하는 간결한 코드

#### Syntax

```python
newDict1 = {key: value for variable in iterable}
newDict2 = {key: value for variable in iterable if condition}
```

```python
# ex code

```

## loop control

반복문 제어

### break

반복문 종료

### continue

다음 반복 수행

### pass

아무것도 하지 않음(있으나 마나)

### for-else

끝까지 반복문 실행한 이후에 else문 실행

반복문 잘 끝났나 확인하는 용도로 많이 쓴다.