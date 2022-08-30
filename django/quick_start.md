# 장고 빠른 시작

- [python 가상 환경 문서](../python/module/virtual_environment.md) 참고

## LTS

- LTS(Long Term Support, 장기 지원 버전)

- 장기간에 걸쳐 지원하도록 고안된 소프트웨어 버전

- 컴퓨터 소프트웨어 제품 수명주기 관리 정책

- 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함.

## Django Application

- 하나의 장고 프로젝트에는 여러 App이 들어갈 수 있다.(하나도 가능)

- 기능별로 App을 나눠서 개발한다.

- `python manage.py startapp articles` 앱 생성

    - views.py

- 앱 등록(프로젝트에게 앱에 대해서 알려주기)

    - `settings`에 `INSTALLED_APPS`에 추가하기

### App

- `migrations` 데이터베이서 변경 히스토리가 남는 곳

- `tests.py` 테스트 케이스를 넣어두는 곳

> models와 views를 중점적으로 보자

- `models.py` (데이터)

- `views.py` (연결)