# Migrations

- 작성한 models.py는 DB Table Schema를 설계한 것

> 이제 DB 설계도를 만들어보자.

- **Migrations** : Django가 모델에 생긴 변화(필드 추가, 수정 등)를 실제 DB에 반영하는 방법

## Migrations 관련 주요 명령어

> 중요! 명령어 이름 체크!

### makemigrations

- `python managa.py makemigrations`

- **migration 파일**이 만들어짐. Django가 models.py에 작성한 스키마 정보를 기반으로 한 최종 설계도(DB)를 만들어 준 것

- 마이그레이션 파일이 DB 설계도(blue-print)

- **아직 DB에 반영된 것은 아님**(테이블 안 생김)

### migrate

- makemigrations로 만든 **설계도를 실제 DB**(db.sqlite3 파일)에 **반영**(모델과 DB 동기화)

- `python manage.py migrate`

- 내부적으로 마이그레이션 파일이 apply됐다.

> 내가 만든 것을 제외한 수 많은 설계도는 무엇일까?
> - 우리가 직접 만든 앱은 하나지만, django를 구동하기 위한 기본적인 내장 앱들이 존재한다. (settings.py에서 확인할 수 있다.)
> - 이 앱들도 DB를 쓰고, DB에 테이블이 필요.
> - 그래서 처음 migrate 할 때, 이 내장 앱들의 설계도도 함께 apply 되서, 테이블이 만들어진다.

## Migrations 기타 명령어

### showmigrations

-  `python manage.py showmigrations` 

- 마이그레이션이 됐는지 확인하는 명령어

### sqlmigrate

- `python manage.py sqlmigrate app_name 0001`

- 해당 migrations 파일이 SQL 문으로 어떻게 해석 될 지 미리 확인할 수 있다.

## DB 파일 열어보기

- DB 파일을 열어보면 테이블들이 많이 보인다!

    - 테이블 이름은 `appname_classname`이다.

## 설계도는 누가, 어떻게 해석할까?

- 파이썬 언어를 SQL로 바꿔주는 것이 ORM