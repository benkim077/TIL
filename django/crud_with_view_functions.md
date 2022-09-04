# CRUD with View Functions

> QuerySet API를 통해 view 함수에서 CRUD 구현하기

> 세부 내용은 따로 적지 않음

## HTTP response status code

> HTTP 요청이 완료되었는지 여부를 코드를 보고 알 수 있다.

- 5개 그룹

1. Informational responses(1XX)

2. **Successful responses(2XX) - 성공**

3. Redirection messages(3XX)

4. **Client error responses(4XX) - 클라이언트 에러**

5. **Server error responses(5XX) - 서버 에러**

## HTTP request method

- HTTP는 request method를 정의하여, 주어진 리소스에 수행하길 원하는 행동을 나타냄

### HTTP method GET

- GET은 **데이터를 얻을 때만** 사용(Read 역할)

### HTTP method POST

- 서버로 데이터 전송

- **DB를 수정하는 모든 연산**(Create, Update, Delete 역할)

- URL로 보내지지 않음

#### CSRF Cross-Site-Request-Forgery

- 사이트 간 요청 위조

- Security Token 사용 방식(**CSRF Token**)

    - 사용자의 데이터에 임의 난수 값(token)을 부여해 매 요청마다 포함시켜 전송

    - 서버에서 요청을 받을 때 마다 token 값이 유효한지 검증

    - 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용

- `{% csrf_token %}`