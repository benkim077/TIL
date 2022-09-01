# Django Model

- MTV 디자인 패턴 중 마지막. Model

- Model을 통해서 DB를 조작할 수 있다.

- 데이터 구조화 및 조작하는 역할

## Model

- DB를 컨트롤할 수 있게 해주는 도구(추상적인 객체)

- 사용하는 데이터들의 필수적인 필드들과 동작들이 포함됨.

    - 필드(컬럼), 동작(인스턴스의 메서드)

- **필드와 인스턴스**를 통해서 DB 구조 만든다.

- 하나의 **모델 클래스**가 만들어지고 이것이 **테이블 하나**가 된다.

- 우리는 django Model을 통해서 **간접적으로 DB에 접근 및 조작**할 것이다.

- 모델과 DB는 다름. DB에 직접 접근하지 않고, 모델을 통한 데이터를 관리한다..

### (참고) 매핑 Mapping

- 하나의 값을 다른 값으로 대응, 연결

## Models.py 작성

- 모델 클래스를 작성하는 것은 DB Table Schema를 정의하는 것

- 모델 클래스 == 테이블 스키마

### 1

- 각 모델은 django.models.Model 클래스의 서브 클래스

    - 각 모델은 django.db.models 모듈의 Model 클래스를 상속받아 구성

### 2

- models 모듈을 통해 어떠한 타입의 DB 필드(컬럼)을 정의할 것인지 정의

- 클래스 변수는 DB의 필드(컬럼)을 정의하는 부분

    - 앱에 어떤 데이터 구조(스키마)가 필요한지 정의

### 3

- 클래스 변수명은 DB 필드의 이름

- 클래스 변수 값(models 모듈의 Field 클래스)은 DB 필드의 데이터 타입

## 장고 모델 필드

- 모델 필드를 통해 테이블의 컬럼(필드) 저장할 데이터 유형을 정의

- 데이터 유형에 따라 다양한 모델 필드를 제공

    - DataField(), CharField(), IntegerField() 등

### CharField

- `CharField(max_length=None, **options)`

- 길이 제한 문자열을 넣을 때 사용

- `max_length`가 DB와 Django의 유효성 검사(값 검증)에서 활용

### TextField

- `TextField(**options)`

- 글자 수가 많을 때 사용