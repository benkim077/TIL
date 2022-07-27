# 객체와 클래스 문법

> 클래스와 인스턴스의 기본 문법에 대해서 알아보자.

## 기본 문법

- 클래스 선언

```python
class MyClass:
    pass
```

- 인스턴스 선언

```python
my_instance = MyClass()
```

- 인스턴스 메서드 호출

```python
my_instance.my_method()
```

- 인스턴스 속성 호출

```python
my_instance.my_attribute
```

## 클래스와 인스턴스

> 클래스와 인스턴스의 타입은?

```python
class Person:
    pass

print(type(Person)) # <class 'type'>

person1 = Person()

print(isinstance(Person1, Person)) # True
print(type(Person1)) # <class '__main__.Person'>
```

## 객체 비교

### == 동등한(equal)

- 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True

    - 내용이 같으면 True

- 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님

### is 동일한(identical)

- 두 변수가 동일한 객체를 가리키는 경우 True

    - 주소가 같으면 True

    - 엄밀한 비교

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b) # True False

a = [1, 2, 3]
b = a

print(a == b, a is b) # True True
```