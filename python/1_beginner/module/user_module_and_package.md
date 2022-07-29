# 사용자 모듈과 패키지

## 패키지

패키지는 여러 모듈/하위 패키지로 구조화

모든 폴더에서는 `__init__.py`를 만들어 패키지로 인식시킨다.

## 패키지 만들기

폴더 구조
- my_package/
  - `__init__.py`
  - check.py
  - calculator/
    - `__init__.py`
    - tools.py

check.py에서 tools.py에서 작성한 기능 사용하기

```python
# tools.py
def add(num1, num2):
  return num1 + num2
```

```python
# check.py
from calculator import tools

print(dir(tools)) # 사용할 수 있는 기능들을 보여준다.

print(tools.add(1, 2)) # 3
```

## `__init__.py`

- 패키지 import할 때 자동으로 실행되는 코드를 넣어준다.

- 모듈을 초기화하는 역할을 한다.

> 던더 이닛을 통해 모듈까지 접근하는 방법

`import my_pac` > `from . import my_mod` > `from . import my_func`