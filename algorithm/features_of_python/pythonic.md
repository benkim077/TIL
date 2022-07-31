# Pythonic

## Intro

파이썬만의 특징, pythonic에 대해서 살펴본다.

## 파이썬 문법

### 타입 힌트

- 동적 타이핑 언어임에도, Type hint 기능

```python
`var_name: type = value` # 변수 type hint

def func_name(parameter: type) -> return_type: # 함수 type hint
    pass
```

- 실제로 적용되진 않지만, 가독성과 에러를 줄이는 데 도움이 된다.

- `pip install mypy` > `$ mypy test.py`

    - type hint에 오류가 있는지 확인할 수 있다.

### 제너레이터

- 루프의 반복 동작을 제어할 수 있는 루틴 형태

- `yield`를 통해 generator 값을 내보낼 수 있는 함수를 만든다.

    - `return`과 비슷지만, 진행된 값을 내보내고 함수는 계속 실행된다.

- `next()`를 통해 다음 값을 추출할 수 있다.

- 제너레이터를 이용하면 조건과 생성을 구분할 수 있다.

    - `range()`는 조건이 들어간 range 객체를 만들어준다.
    
    - 필요할 때 마다 값을 얻어 사용할 수 있다.

### enumerate

- `enumerate()`는 iterable 자료형을 받고, 인덱스가 포함된 enumerate 객체를 리턴한다.

### print

- list를 출력할 때 `join()` 메서드를 이용해서 출력

### locals

- `locals()` 함수는 로컬 심볼 테이블 딕셔너리를 리턴

    - 로컬에 선언된 모든 변수를 딕셔너리 형태로 출력해준다.

## 코딩 스타일

### 리스트 컴프리헨션

- 줄 구분을 하면 가독성이 높은 코드를 작성할 수 있다.

```python
new_list = [
    num ** 2 for num in range(1, 10 + 1)
    if num % 3 == 0
] # [9, 36, 81]
```

### 구글 파이썬 스타일 가이드

- parameter default value에 mutable object(list, dict)를 사용하지 않는다.

    - immutable object(int, str, tuple, None)

- Truthy, Falsy를 쓸 때, 명시적으로 표현한다.

    - 주소를 참조할 땐, is, is not(비교연산자)

    - 값이 없다면(null) not(논리연산자)

    - 값을 참조할 땐, 값을 분명하게 사용한다.