# Function Usage

함수 응용

## 내장 함수(Built-in Functions)

항상 사용할 수 있는 함수와 type 내장

### map

`map(function, iterable)`

iterable의 모든 요소에 function 적용하고, 
그 결과를 map object로 반환

### filter

`filter(function, iterable)`

iterable의 모든 요소에 function 적용하고,
그 결과가 True인 것들을 filter object로 반환

### zip

`zip(*iterables)`

복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

iterable을 세로로 묶는다고 생각

## lambda 함수

`lambda[parameter]: expression`

익명함수. 한 번 쓰고 말 것.

[재귀함수 참고](../lambda.md)

## recursive function 재귀함수

자기 자신을 호출하는 함수

알고리즘 설계 및 구현에서 활용

코드의 가독성 높아짐

1개 이상의 base case가 존재하고, 수렴하도록 작성

### 재귀함수 주의사항

base case에 도달할 때까지 함수를 계속 호출

메모리 스택이 넘치면(stack overflow) 프로그램이 넘치게 않게 됨

파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1,000번으로, 호출 횟수가 이를 넘어가게 되면 Recursion Error 발생

### 재귀함수 반복문으로 표현

재귀함수를 반복문으로, 반복문을 재귀함수로 바꿀 수 있다.

### 재귀함수 반복문 비교

알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용함

재귀 호출은 변수 사용을 줄여줄 수 있음

재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림