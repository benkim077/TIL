# Django 디자인 패턴

> 장고는 MVC 디자인 패턴을 기반의 **MTV 패턴**을 사용한다.

## MVC 디자인 패턴

> Model - View - Controller design pattern

- 하나의 프로그램을 세 가지 역할로 구분한 개발 방법론

    1. Model: 데이터와 관련된 로직 처리

    2. View: 화면과 레이아웃 처리

    3. Controller: model, view를 연결, 중계(중간 처리 및 응답 반환)

- 목적 : 업무 분리, 관리 향상, 체계화, 협업

## MTV 패턴 ✅

- **Model** 데이터

- **Template** 화면

- **View** 연결

## MTV 구조 흐름

1. HTTP Request

2. URLS : Foward request to appropriate view

3. View : Function Call 

4. Model(data handling) or Template(rendering web page)

5. Back to View, return HTTP Response(HTML)