# 장고 빠른 시작

## 가상 환경 세팅하기

- `$ python -m venv venv` 빈 가상 환경 생성
cd .
- `source ./venv/Scripts/activate` 가상환경 활성화

- `pip list` 패키지 리스트 확인

- `pip install django==3.2.13` 장고 특정 버전 설치

- `pip freeze > requirements.txt` 설정 저장하기

- `pip install -r requirements.txt` 설정 불러오기

## 새 장고 프로젝트 시작하기

- `django-admin startproject pjt_name .` 현재 위치에 새 프로젝트 만들기

- `python manage.py runserver` 서버 실행하기

- `Ctrl + C` 서버 닫기

### 프로젝트 파일 설명

> settings.py, urls.py 만 살펴보자

- `manage.py` 장고 프로젝트에 대한 명령 수행

- `db.sqlite3` 데이터베이스 파일

- `urls.py` urls를 분기해서, 알맞은 view에 전달. (우편 배달부)

- `asgi.py`, `wsgi.py` 동기, 비동기(나중에 다시)

- `settings.py` 장고 프로젝트 전반에 대한 세팅

## 장고 앱 Django Application

- 앱은 프로젝트의 한 기능이라 볼 수 있다.

- 하나의 장고 프로젝트에는 여러 App이 들어갈 수 있다.(하나도 가능)

- 기능별로 App을 나눠서 개발한다.

- `python manage.py startapp app_name_s` 앱 생성 명령어

- `settings`에 `INSTALLED_APPS`에 추가하기(프로젝트에 앱 등록)

> 반드시 생성 후 등록

### 앱 파일

> models와 views를 중점적으로 보자

- `admin.py` 관리자용 페이지 설정

- `app.py` 앱 정보가 들어있음. 별도 작성 X

- `models.py` 앱에서 사용하는 Model을 정의(데이터 처리)

- `tests.py` 테스트 코드를 작성하는 곳

- `view.py` 앱에서 사용하는 view를 정의(연결)

- `migrations/` 데이터베이서 변경 히스토리가 남는 곳