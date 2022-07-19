## Arithmetic Operator

산술 연산자

## Comparison Operator

비교 연산자

- \>, \>=, \<, \<=
- == 같음
- != 같지 않음
- is 객체 아이덴티티(OOP)
- is not 객체 아이덴티티가 아닌 경우

## Logical Operator

논리 연산자

- A and B  모두 True → True
- A or B  모두 False → False
- Not  True → False, False → True
- **우선순위 not > and > or**

```python
print(not True and False or not False) # True
```

### Truthy Falsy

**False는 아니지만, False로 취급되는 다양한 값 Falsy**

- 0
- 0.0
- ()
- []
- {}
- None
- ''(빈 문자열)

Falsy가 아닌 값은 모두 **Truthy**

### 논리 연산자의 단축 평가

**단축 평가가 되게 하는 부분의 표현식이 전체 표현문의 값이 된다.** 

-  and는 a가 거짓이면 a를 리턴, 참이면 b를 리턴
-  or은 a가 참이면 a를 리턴, 거짓이면 b를 리턴

- **결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째 값 반환**
    - and  첫 값이 False인 경우 무조건 False ⇒ 첫번째 값 반환
    - or  첫 값이 True인 경우 무조건 True ⇒ 첫번째 값 반환

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


## Identity Operator

식별 연산자
`is`연산자를 통해 동일한 object인지 확인할 수 있다.

```python
a, b = 3, 3
print(a is b) # True
print(id(a), id(b)) 
# id가 같다는 것은 같은 object라는 뜻.
# id()는 객체의 메모리 주소이다. 
```

## Membership Operator

멤버십 연산자
요소가 시퀀스에 속해있는지 확인할 수 있다.

- `in` 연산자
- `not in` 연산자

```python
'a' in 'apple' # True
1 in [3, 2, 1] # True
```