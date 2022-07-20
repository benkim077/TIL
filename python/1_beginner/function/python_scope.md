# Python Scope

scope와 variable의 관계

scope
- local scope
  - 함수가 만든 scope. 
  - 함수 내부에서만 참조 가능
- global scope
  - 어디에서든 참조할 수 있는 공간

variable
- local variable 로컬 변수
  - 로컬 스코프에 정의된 변수
- global variable 글로벌 변수
  - 글로벌 스코프에 정의된 변수

## 변수 수명주기(lifecycle)

- built-in scope
파이썬이 실행된 이후부터 영원히 유지

- global scope
모듈이 호출된 시점 이후 혹은 인터프러터가 끝날 때까지 유지

- local scope
함수가 호출될 때 생성, 종료될 때까지 유지

## 이름 검색 규칙(Name Resolution)

파이썬에서 사용되는 이름들은 이름공간(namespace)에 저장되어 있음

이름을 찾아가는 scope 순서. LEGB Rule

- Local scope
  - 지역 범위
  - 현재 작업 중인 범위
- Enclosed scope
  - 지역 범위 한 단계 위 범위
- Global scope
  -  최상단에 위치한 범위
- Built-in scope
  - 모든 것을 담고 있는 범위
  - 정의하지 않고 사용할 수 있는 모든 것
  - ex) print

**함수 내에서 바깥 scope의 변수에 접근 가능하나 수정은 할 수 없음**

## global 문

현재 코드 블록 전체에 적용.

나열된 식별자가 global variable임을 나타냄

주의사항
- global에 나열된 식별자는 같은 코드 블록에서 global 앞에 등장할 수 없음
- global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 등으로 정의되지 않아야 함.

## nonlocal

global을 제외하고 가장 가까운(둘러싸고 있는) scope의 변수를 연결하도록 함

global과 달리 이미 존재하는 이름과의 연결만 가능함

## 함수의 범위 주의

global, nonlocal 키워드는 지양
=> argument, return값을 사용하는 것을 추천