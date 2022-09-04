# Model 2

> **models.py에 변경사항**이 생겼을 때, 해야 하는 migration에 대해 알아본다.

## 테이블에 Column 추가하기

- 추가필드 `created_at = models.DataTimeField(auto_now_add=True)`

- 이후 **makemigrations 명령어**를 실행하면, django가 컬럼의 기본값 설정에 대해 물어본다.

    - 이미 존재하는 테이블에 새로운 컬럼이 추가될 때, 빈 값으로 추가될 수 없기 때문에, 기본값 설정을 한다.

## DateTimeField()

- Python의 datetime.datetime 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드

- DataField를 상속받는 클래스

- 선택 인자

    1. auto_now_add

        - 최초 생성 일자 creation of timestamps

    2. auto_now

        - 최종 수정 일자 last-modified