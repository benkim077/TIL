# 얕은 복사와 깊은 복사 Shallow Copy & Deep Copy

> Python은 항상 객체의 주소값을 들고온다.

복사 방법 3가지 

- 할당 (assignment)

- 얕은 복사 (shallow copy)

- 깊은 복사 (deep copy)

## 할당

할당 연산자

> 할당해서 둘 중 하나만 바꿨는데 둘 다 바뀌네?

대입 연산자를 통한 복사는 **해당 객체에 대한 객체 참조를 복사**한다.

## 얕은 복사

- Slice 연산자 활용하면, 결과를 복사(다른 주소)

- 결과를 복사해서 다른 객체를 만들고 참조함.

복사하는 리스트의 원소가 주소를 참조하는 경우도 있다.

- 1차원 리스트만 복사하고, 2차원 리스트는 참조를 복사한다.

> 해결책 Deep Copy

## 깊은 복사

```python
import copy # copy 모듈

a = [1, 2, ['a','b']]
b = copy.deepcopy(a) # deepcopy 함수

b[2][0] = 0

print(a, b) # [1, 2, ['a', 'b']], [1, 2, [0, 'b']]
```

> list를 복사할 때 deepcopy를 써야겠다.