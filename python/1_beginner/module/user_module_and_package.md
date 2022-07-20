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

## 모듈 만들기

## 모듈 활용하기