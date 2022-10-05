# N 대 1 관계

- 관계형 DB에서 외래 키를 이용해 모델간 N:1 관계 설정하기

- 기본 키 : 테이블에서 행을 고유하게 식별 가능하게 하는 속성

- 외래 키 : 각 행에서 서로 다른 테이블 간 관계를 만드는 데 사용

- 관계 : 테이블 간 상호작용을 기반으로 한 논리적 연결

    - 1:1 관계, N:1 관계, M:N 관계

## Foreign Key

- 외래 키, 외부 키

- 관계형 DB에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키

- 참조되는 테이블의 기본키를 가리킴

### 특징

- 키를 사용하여 부모 테이블(참조되는 테이블)의 유일한 값을 참조(참조 무결성)

- 외래 키 값이 반드시 부모 테이블의 기본키일 필요는 없지만, 유일한(UNICUE) 값이어야 함

- 참조 무결성

    - DB 관계 모델에서, 관련된 2개의 테이블 간의 일관성을 말함

    - 외래 키가 선언된 테이블의 외래키 속성 값은 부모 테이블의 기본키 값이 되어야 함.

## Django Relationship fields 

- 장고 관계 필드

- 종류

    1. OneToOneField()

    2. ForeignKey()

    3. ManyToManyField()

- `ForeignKey(to, on_delete, **options)`

    - N:1 관계를 담당하는 장고 모델 필드 클래스

    - 장고 모델에서 관계형 DB의 외래 키 속성을 담당

    - 2개의 필수 인자(참조하는 모델 클래스, on_delete 옵션)

### ForeignKey

- ForeignKey() 클래스의 인스턴스 이름은 참조 모델 클래스 이름의 단수형으로 작성

    - 컬럼 이름이 `인스턴스명_id`로 작성된다.

- on_delete

    - 외래키가 참조하는 객체가 사라졌을 때, 외래키를 가진 객체를 어떻게 처리할 지를 정의

    - 데이터 무결성을 위해서 매우 중요한 설정

    - CASCADE : 부모객체가 삭제되면, 참조하는 객체도 삭제

    - PROTECT, SET_NULL, SET_DEFAULT 등

- 데이터 무결성(Data Integrity)

    - 데이터의 정확성, 일관성을 유지하고 보증

    - DB, RDBMS의 중요한 기능

    - 무결성 제한의 유형 : 개체 무결성, 참조 무결성, 범위 무결성

## Related manager

- 관계 모델 참조

- Related manager는 N:1 혹은 M:N관계에서 사용 가능한 문맥(context)

- 장고는 N:1, M:N 관계가 설정되면 **역참조**에 사용할 수 있는 manager를 생성

- related manager를 통해 queryset api를 사용할 수 있다.

### 역참조

- 나를 참조하는 테이블을 참조하는 것

- 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것

### comment_set manager

- `article.comment_set.method()`

- Article 모델이 Comment 모델을 참조(역참조)할 때 사용하는 매니저

- 장고는 역참조할 수 있는 comment_set manager를 자동으로 생성. `article.comment_set` 형태로 댓글 객체를 참조할 수 있다.

    - N:1 관계에서 related manager는 '모델명_set' 이름 규칙으로 만들어진다.

```python
# shell_plus
article = Article.obejects.get(pk=1)
article.comment_set.all()       # => Comment 쿼리셋을 리턴
```

### ForeignKey arguments - ralated_name

`article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')`

- ForeignKey 클래스의 선택 옵션

- 역참조 시 사용하는 매니저 이름을 변경할 수 있음

- 반드시 작성해야 하는 경우가 있음