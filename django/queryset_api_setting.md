# 사전 준비

> 실습 편의를 위한 추가 라이브러리 설치 및 설정

- `$ pip install ipython`, `$ pip install django-extensions` 

    - `django_extensions`는 `settings.py`에 추가하기

- ipython

    - 기본 쉘 보다 더 강력한 파이썬 쉘

- django-extensions

    - django 확장 프로그램 모음

    - shell_plus, graph model 등 다양한 확장 기능

> 패키지 목록 업데이트 하기

- `$ pip freeze > requirements.txt`

## (참고) Shell

- **사용자와 운영체제 간의 인터페이스**를 제공하는 프로그램

- 파이썬 쉘은 파이썬 코드와 소통하는 것

- 파이썬 인터프리터라고도 한다.

- 인터렉티브 또는 대화형 쉘이라고 부른다.

- 쉘 나갈 때는 `exit()`

## Django Shell

> 파이썬 쉘은 파이썬 파일을 읽어서 파이썬과 소통

> 장고 쉘은 장고 프로젝트와 소통하는 것

- `$ python manage.py shell_plus`

- 파이썬 쉘이 장고 환경에서 켜진다.

- 켜지기 전에 from, import. 장고에서 자주 사용하는 클래스, 메서드, 모듈을 자동으로 임포트해주고 시작.

- 우리가 만든 것도 있다.
