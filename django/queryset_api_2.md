# 쿼리셋 API 익히기

> Queryset API를 활용해 데이터를 CRUD 해보기

## CREATE

> 3가지 방법

> 2번 방법 사용. 데이터를 받은 후 검증Validation을 하고 세이브를 한다.

### 방법 1

- `article = Article()` 클래스를 통한 인스턴스 생성

- `article.title = value` 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당

- `article.save()` 인스턴스로 save 메서드 호출

### 방법 2

- `article = Article(title = value1, content = value2)`

- `article.save()`

### 방법 3

- `Article.objects.create(title=value1, content=value2)`

- QuerySet API 중 create() 메서드 활용

- save() 메서드가 필요 없음. 바로 생성된 데이터가 반환된다.

### .save() 메서드

- 객체를 DB에 저장

- model 클래스를 통해 인스턴스를 생성하는 것은 DB에 영향을 미치지 않음. 

- save를 호출해야 테이블에 레코드 생성

## READ

- **어떻게** 조회할 것인가?

- 2가지로 분류

    - 쿼리셋을 받느냐(데이터 목록)

    - 쿼리셋을 받지 않느냐(데이터 하나)

### all()

- QuerySet을 리턴

- 전체 데이터를 조회

### get()

- 단일 데이터 조회

    - 찾을 수 없으면 DoesNotExist 예외

    - 둘 이상이면 MultipleObjectsReturned 예외

- 즉, 유니크한 값에만 사용(PK). 

- 고유성을 보장하는 조회에서 사용해야 함

### filter()

- 지정된 조회 매개변수와 일치하는 객체를 포함하는 QuerySet을 반환

- 데이터가 없으면 빈 쿼리셋을 반환(에러가 안뜸)

- 조회된 객체가 없거나 1개여도 무조건 새로운 QuerySet을 반환

> PK를 조회할 때 filter를 사용하지 않는 이유?

1. 쿼리셋 내부에 한 번 더 접근해야 함

2. 데이터가 없다면, 예외를 발생시켜야 하는데, 발생시키지 않음

### Field lookups

- 특정 레코드에 대한 조건을 설정하는 방법

- 쿼리셋 메서드에 대한 키워드 인자로 지정

- `Article.objects.filter(content__contatins='dj')` content 컬럼에서 'dj'가 포함된 모든 데이터 조회

## UPDATE

- `article = Article.objects.get(pk=1)` (수정 전에 먼저 해야될 것) 수정하고자 하는 객체를 먼저 조회해서 변수에 저장

- `article.title = 'byebye'` 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당

- `article.save()` 인스턴스 메서드 호출. DB에 저장

## DELETE

- `article = Article.objects.get(pk=1)` 삭제하고자 하는 article 인스턴스 객체를 조회 후 반환 값 저장

- `article.delete()` delete() 인스턴스 메서드 호출

- 삭제된 id는 재사용하지 않음

## 참고(출력 바꾸는 방법)

- `__str__`를 정의하여 각각의 object가 문자열을 리턴하도록 할 수 있다.