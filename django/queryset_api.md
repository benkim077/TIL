# Query Set API

> Query Set API를 사용해서 DB로 전달, QuerySet은 DB로부터 정보를 받는 것

## Database API

- 장고가 제공하는 ORM을 사용해 DB를 조작하는 방법

- **Model을 정의하면**, Django가 데이터를 만들고 읽고 수정하고 지울 수 있는 **API를 제공**해준다.

### DB API 구문

- `Article.objects.all()`

    - Article은 정의한 **model class**

    - **objects는 Manager**. ('하인'에게 다 시키자)

    - `all()`이 **Queryset API**

#### object manager

- 장고와 DB가 소통할 때, 쿼리 작업이 가능하도록 하는 **인터페이스**

- **다양한 쿼리셋 API를 제공**. 여러 메서드를 제공한다.

## Query

> Query는 DB에게 하는 요청이다.

- ORM은 파이썬 코드를 받아 SQL(Structured Query Language)로 변환해서 DB로 요청을 전달

- ORM은 **DB의 응답 데이터**를 받아, **QuerySet이라는 자료 형태**로 변환하여 우리에게 전달

### QuerySet

- DB로 부터 데이터를 쿼리셋 형태(데이터 객체 목록)로 가져온다.

    - iterable data. 1개 이상의 데이터. 인덱스로 접근 가능.

    - ORM을 통해 만들어진 자료형. 필터, 정렬 등을 수행할 수 있음

- 복수가 아닌 단일 객체가 반환될 때는 모델 클래스의 인스턴스가 반환된다.

#### QuerySet API

- 쿼리셋과 상호작용하기 위해 사용하는 도구(메서드, 연산자 등)