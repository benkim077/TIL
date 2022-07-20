# 파이썬 표준 라이브러리

## 파이썬에 기본적으로 설치된 모듈과 내장 함수

파이썬에 기본적으로 설치된 모듈과 내장 함수

## 파이썬 패키지 관리자(pip)

PyPi(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

### 명령어

### 패키지 설치

- 최신 버전 / 특정 버전 / 최소 버전 명시 설치

`$ pip install SomePackage`
`$ pip install SomePackage==version`

### 패키지 삭제

`$ pip uninstall SomePackage`

### 패키지 목록 및 특정 패키지 정보

`$ pip list`
`$ pip show`

### 패키지 관리하기

`$ pip freeze > requirements.txt` pip list 저장 
`$ pip install -r requirements.txt` 저장한 것 인스톨. -r 은 반복