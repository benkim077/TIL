# 다형성 Polymorphism

- 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미

- 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 다른 방식으로 응답할 수 있음

> 다형성은 추상적 개념이다. 
>
> 구체적 기법에는 오버라이딩과 오버로딩이 있다.

## 메서드 오버라이딩 Method Overriding

- 상속받은 메서드를 재정의

    - 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경

    - 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용

- 상속받은 클래스에서 같은 이름의 메서드로 덮어쓴다.

- 부모 클래스의 메서드를 실행시키고 싶은 경우 

    - `super().method()`를 활용

### (번외) 오버로딩 Overloading

> 오버로딩은 같은 이름의 메서드를 다르게 정의하여 사용할 수 있는 방법이다.

- 파이썬에서 오버로딩은 공식적으로 지원하지 않는다.

- 파이썬에서 오버로딩은 가변인자(*args)로 구현할 수 있다.