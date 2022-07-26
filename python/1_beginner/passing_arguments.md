# Passing Arguments

함수 인수 전달 방식

## intro

```python
# 파이썬에서 for 문을 이용해 list element의 값을 변경하려고 한다.
my_list = [1, 2, 3]

for element in my_list:
    element = 0

print(my_list) # [1, 2, 3]
```

왜 my_list는 바뀌지 않았을까?

element가 my_list의 요소의 값을 복사했기 때문이다.

## Call By Reference & Call by Value

함수를 호출할 때, 함수에 argument를 전달하는 방식은 다음과 같다.

- Call by value 값에 의한 호출

- Call by reference 참조에 의한 호출

### Call by Value

element는 my_list에서 **값**을 불러와서 사용한다.(Call by Value)

element는 my_list의 실제 요소가 아니라, **값을 복사**한 것이다. 즉 둘은 별개다.

값을 복사해서 호출한다. 

### Call by Reference 참조에 의한 호출

반면 Call by Reference는 주소를 참조하여 호출한다.

## Call by Assignment in Python

파이썬에선 call by assignment 방식.

call by assignment란, 전달받는 객체에 따라 객체의 참조방식이 결정된다는 의미이다.

이때, 객체의 종류를 mutable, immutable object로 나눌 수 있다.

### Mutable Object

list, dict, set type

### Immutable Object

str, int, tuple

