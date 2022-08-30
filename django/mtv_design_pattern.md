# Django 디자인 패턴

- 장고는 MVC 디자인 패턴을 기반으로한, MTV 패턴을 사용한다.

## MVC 디자인 패턴

- Model - View - Controller

- 하나의 프로그램을 세 가지 역할로 구분한 개발 방법론

1. Model: 데이터와 관련된 로직 처리

2. View: 화면과 레이아웃 처리

3. Controller: model, view를 연결, 중계(중간 처리 및 응답 반환)

### 목적

- 관심사 분리

- 업무 분리, 관리 향상, 체계화, 협업

## MTV 패턴

- (Model ->) Model 데이터

- (View ->) Template 화면

- (Controller ->) View 연결

## MTV 구조 흐름

1. HTTP Request

2. URLs(urls.py) : Foward request to appropriate view

3. View(views.py)

4. Model(models.py) or Template(<filename>.html)

5. View

6. HTTP Response(HTML)