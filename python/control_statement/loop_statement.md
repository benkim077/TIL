# 반복문

## while

- 조건이 참인 경우 반복적으로 코드 실행

- **조건**을 알고 있을 때 while을 사용하자.

## for

- **iterable object의 element를 모두 순회**

- **범위**를 알고 있다면 for를 사용하자.

### What is iterable?
  - Data Type

    - string, list, dict, tuple, set

  - iterable function

    - range, enumerate

### Syntax

```python
for element in iterable:
  pass
```

### Dictionary 순회

- 기본으로 key를 순회, 루프 안에서 `dict[key]`로 value에 접근

```python
# dict의 값, type에 대해 잠시 확인해보자.
my_dict = {'영어': 'Hello', '한국어': '안녕하세요'}
print(my_dict) # {'영어': 'Hello', '한국어': '안녕하세요'}
print(type(my_dict)) # <class 'dict'>
print(my_dict.items()) # dict_items([('영어', 'Hello'), ('한국어', '안녕하세요')])
print(type(my_dict.items())) # <class 'dict_items'>
```

#### 메서드 활용 순회

**dict를 iterable로 활용하려면, 메서드를 사용해야 한다.**

- keys(), values()

  - list 리턴 

  - `dict_keys(['k1', 'k2'])` `dict_values([v1, v2])`

items()
- list 안에 튜플 리턴 
- `dict_items([('k1', v1), ('k2', v2)])`

### Enumerate 순회

- **(idx, value) 튜플**로 구성된 열거(enumerate) **객체 반환**

- idx와 value를 같이 쓰고 싶을 때 사용한다.

#### Syntax

```python
# enumerate(iterable[,start=0])
members = ['kim', 'lee', 'park']
list(enumerate(members)) # [(0, 'kim'), (1, 'lee'), (2, 'park')]
```

```python
members = ['kim', 'lee', 'park']
for idx, name in enumerate(members, start=1): # 
    print(idx, name)
```

### List Comprehension

- 기존 iterable에서, **조건**을 만족하는 **새로운 리스트**를 짧고 간결하게 생성할 수 있는 문법이다.

- comprehension 기능 굳이 쓸 필욘 없다. **가독성이 안 좋다.** python에 익숙해지면 도전하자.

[w3s - list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)

#### Syntax

```python
# 문법이 복잡하지만 코드를 읽으면 문맥이 있다.
newList = [expression for element in iterable if condition] # 조건이 참일 때, iterable의 element에 대해서, expression list를 새로 만든다.
```

```python
# ex1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) # ['apple', 'banana', 'mango']
```

```python
# ex2
newlist = [x for x in range(10) if x < 5] # [0, 1, 2, 3, 4]
```

### Dictionarary Comprehension

list comprehension과 유사하나, dictionary로 평가되는 표현식

[programiz - dictionary comprehension](https://www.programiz.com/python-programming/dictionary-comprehension)

#### Syntax

```python
newDict1 = {key: value for item in iterable}
newDict2 = {key: value for item in iterable if condition}
```

```python
# 달러 가격을 원화 가격으로 변경
usdPrice = {'milk': 1, 'coffee': 3, 'bread': 2}
DOLLAR_TO_KRW = 1300

krwPrice = {item: value*DOLLAR_TO_KRW for (item, value) in usdPrice.items()}
print(krwPrice)
```

## loop control

- 반복문 제어

### break

- 반복문 종료

### continue

- 다음 반복 수행

### pass

- 아무것도 하지 않음

- 구조 잡을 때 사용

### for-else

- 끝까지 반복문 실행한 이후에 else문 실행

반복문 잘 끝났나 확인하는 용도로 많이 쓴다.