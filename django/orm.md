# ORM Object-Relational-Mapping

- 객체 지향 프로그래밍 언어를 사용하여 **호환되지 않는 유형의 시스템 간**에(django <-> SQL) **데이터를 변환**하는 프로그래밍 기술

- Django ORM (장고 내장 ORM)

- **SQL을 사용하지 않고 DB를 조작**할 수 있게 만들어주는 **매개체**(Python과 SQL의 **인터페이스**)

    - Python Object -> ORM -> SQL

    - SQL -> ORM -> Python Object

> Python Object를 잘 보내고, 잘 받으면 된다.

## ORM의 장단점

### 장점

- SQL을 몰라도 객체지향 언어로 DB 조작 가능

- 객체 지향적 접근으로 높은 **생산성**(빠르게)

### 단점

- ORM 만으로 세밀한 DB 조작을 구현하기 어렵다.

    - 언젠가는 SQL이 필요하다.