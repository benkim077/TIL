# 가상환경

파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우
모두 pip를 통해 설치해야 함

복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
- 과거 외주 프로젝트(2v)
- 신규 회사 프로젝트(3v)

특정 디렉토리에 가상 환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음

가상 환경을 만들고 관리하는데 사용되는 모듈(3.5v +)

## 가상환경 생성

`$ python -m venv venv`

텅 빈 가상 환경을 만들 수 있다.

## 가상환경 명령어

- `source ./venv/Scripts/activate` 가상환경 활성화 시키기

- `pip list` 패키지 리스트 확인

- `pip install django==3.2.13` 장고 설치하기

- `pip freeze > requirements.txt` 설정 저장하기

- `pip install -r requirements.txt` 설정 불러오기

- `django-admin startproject firstpjt .` (현재 위치에) 새로운 프로젝트 만들기

- `python manage.py runserver` 서버 실행하기

- `ctrl c` 서버 닫기