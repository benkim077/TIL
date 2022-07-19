# 변수 Variable

- **‘데이터 저장 → 처리’가 프로그래밍의 핵심**
- **객체를 참조**하기 위해 사용되는 이름
- 변수는 **데이터 1개를 저장할 수 있는 자료구조**
- 복잡한 값들을 쉽게 사용(**추상화**)

## 변수의 할당 assignment

- 할당 연산자 (=)
- 각 변수의 값을 바꿔서 저장하기

```python
# pythonic
x = 10
y = 20
x, y = y, x
print(x, y) # => 20 10
```

## 식별자 identifier

식별자는 식별하는데 사용되는 이름이다.

- 식별자 이름은 **영문 알파벳 _ 숫자**
- 첫 글자에 숫자 X
- 대소문자 구별
- keyword는 예약어. 식별자 이름으로 사용할 수 없음(keyword.kwlist)

```python
import keyword
print(keyword.kwlist)
```

- 내장 함수나 모듈 등도 사용하지 말아야 한다.

