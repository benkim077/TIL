# Sending and Retrieving Form Data

- 데이터 보내고 가져오기

## Sending Form Data

> 서버로 데이터 보내기

- HTML `<form>` element 의 핵심 속성

    - `action` 입력 데이터를 **어디로** 보낼지
    
    - `method` 데이터를 **어떤 방식으로** 보낼지

        - GET, POST 방식

### input element의 name 속성

- form을 통해 submit했을 때, **name 속성은 서버에서 사용하는 값**이 된다.

- **name은 key, value는 value로 매핑**

## HTTP request methods

- HTTP는 웹에서 데이터 교환의 규칙

- HTTP는 주어진 리소스가 수행할 작업을 나타내는 **request methods**를 정의함.

    - 주어진 자원에 수행하길 원하는 행동

- GET, POST, PUT, DELETE

### GET 방식

- 서버로부터 정보를 조회하는 데 사용

    - 리소스 요청, 데이터 가져올 때

- **Query String**으로 데이터 전송

    - URL에 데이터 포함시켜서 서버로 전송

    - **&로 연결된 key=value 쌍**으로 구성

    - **기본 URL과 ?로 구분**

## Retrieving the Data

> 서버에서 데이터 가져오기

- key-value 쌍의 데이터들을 어떻게 사용할까?

- 모든 요청 데이터는 `view` 함수의 첫 번째 인자 `request`에 들어있다.

- `views.py`에서 `message = request.GET.get('message')`로 가져온다.

- `context`에 `message`를 넣어 `templates`에 보낸다.

## (정리) 요청과 응답 객체 흐름

1. 요청이 발생하면, django는 요청에 대한 메타데이터를 포함하는 `HttpRequest object` 생성

2. 적절한 view 함수 호출, HttpRequest를 첫 번째 인자로 전달

3. view 함수는 `HttpResponse object`를 반환