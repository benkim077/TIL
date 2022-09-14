# Limiting access to logged-in users

- 접근 제어 중 가장 기본적인 로그인 여부로 접근 제한하기 해보자.

- 로그인 사용자에 대한 접근 제한하기(로그인 페이지, 회원가입 페이지)

- 2가지 방법

    1. The raw way

        - `is_authenticated` attribute

    2. The `login_required` decorator

## 

- User model의 속성 중 하나

- 사용자가 인증 되었는지 여부를 알 수 있는 방법

- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성

    - AnonymousUser에 대해서는 항상 False

- 일반적으로 request.user에서 이 속성을 사용 `request.user.is_authenticated`

> (주의) 권한과는 관련이 없으며, 사용자가 활성화 상태이거나 유효한 세선을 가지고 있는지도 확인하지 않음. 로그인 or 비로그인만 확인하는 속성.

## 'next' query string

- 이 부분은 추가내용.

- next를 어떻게 처리해줄지는 선택사항이다.