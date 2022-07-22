# Call By Reference & Call by Value

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

## 함수 인자 전달 방식 Passing argument

함수를 호출할 때, 함수에 argument를 전달하는 방식은 다음과 같다.

- Call by value 값에 의한 호출

- Call by reference 참조에 의한 호출

### Call by Value

element는 my_list에서 **값**을 불러와서 사용한다.(Call by Value)

element는 my_list의 실제 요소가 아니라, **값을 복사**한 것이다. 즉 둘은 별개다.

값을 복사해서 호출한다. 

### Call by Reference 참조에 의한 호출

반면 Call by Reference는 주소를 참조하여 호출한다.

### Call by Assignment

파이썬에선 call by assignment 방식.

## 파이썬은 모든 것이 객체이다?

> 나의 예상 

> 미리 예상해보고, 공부해보자. 지식을 무조건 받아들이지 말자.

## 지역변수, 전역변수와의 관계?

## namespace와의 관계?