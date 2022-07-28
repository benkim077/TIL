# 상속

> 상속을 통해, 부모 클래스의 모든 것을 자식 클래스가 쓸 수 있다!
>
> 코드 재사용성이 높아진다.
>
> 공통점을 찾아내서 클래스로 만들자

- 상속이란

    - 두 클래스 사이 부모-자식 관계를 정립하는 것

    - 자식은 부모에 정의된 속성, 행동, 관계 및 제약 조건 모두 상속받는다.

- 클래스는 상속이 가능함

    - 모든 파이썬 클래스는 object를 상속 받는다.

- 문법

```python
class ChildClass(ParentClass):
    pass
```

## 관련 함수, 메서드

### isinstance(object, classinfo)

- classinfo의 instance거나 subclass인 경우 True

> 보통 isinstance를 사용하고, issubclass는 잘 사용하지 않는다.

### issubclass(class, classinfo)

- class가 classinfo의 subclass이면 True

- classinfo는 클래스 객체의 튜플일 수 있으며, classinfo의 모든 항목을 검사

### super()

> 자식클래스에서 부모클래스의 속성, 메서드를 사용하고 싶은 경우

- 부모 클래스의 요소를 호출할 수 있음

자식 클래스의 생성자 함수를 정의할 때 많이 쓴다.

```python
class Student(Person):
    def __init__(self,..., student_id):
        super().__init__(self,...)
        self.student_id = student_id
``` 

### .mro() 메서드 Method Resolution Order

- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드

- 기존의 인스턴스 - 클래스 순으로 이름 공간 탐색하는 과정에서 상속 관계에 있으면 인스턴스 - 자식클래스 - 부모클래스로 확장

## 다중 상속

- 두 개 이상의 클래스를 상속 받는 경우

- 상속받는 모든 클래스의 요소를 활용 가능

- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정된다.