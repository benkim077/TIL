# Handling HTTP requests ✅

> HTTP requests 처리에 따른 view 함수 구조 변화

- new-create, edit-update의 공통점과 차이점 ✅

    - 공통점 : 공동의 목적(CREATE생성, UPDATE수정)
    
    - 차이점

        - new, edit은 GET 메서드만 처리. (페이지를 렌더링)
    
        - create, update는 POST 메서드만 처리. DB에 조작을 가함(생성/수정)

- 공통점과 차이점을 기반으로 하나의 view 함수에서 HTTP method에 따라 분기처리함(GET, POST) ✅

## CREATE, UPDATE, DELETE 수정 ✅

> create에 new를 넣자.

- request.method 값을 기준으로 new와 create를 나눈다.

- 크게 2가지 부분으로 구분(GET, POST)

- 불필요한 new 관련 데이터 삭제 및 수정

> context 들여쓰기 위치 주의!

- UPDATE, DELETE도 마찬가지로 처리하기(POST or Not POST)