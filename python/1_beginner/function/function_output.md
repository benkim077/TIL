# Function Output

함수 출력

## 값에 따른 함수의 종류

- Void function
  - 명시적 return 값이 없는 경우, **None**을 반환하고 종료
  - ex) print 함수
- Value returning function
  - return 문을 통해 값 반환
  - 값 반환 후 함수가 바로 종료

## print vs return

- print를 사용하면 호출될 때마다 값이 출력
- return은 데이터 처리를 위해 사용

## 두 개 이상의 값 반환

Tuple, list 등 container 활용

```python
def funcName(x, y):
  return x + y, x - y # 튜플로 반환
```