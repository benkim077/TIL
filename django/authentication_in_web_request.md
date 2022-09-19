# Authentication in Web requests

- 장고가 제공하는 인증 관련 **built-in forms** 익히기 ✅

    - **로그인, 회원가입, 비밀번호 변경 등에 사용하는 form을 다 제공**해준다.

## Login ✅

- **로그인은 Session을 CREATE** 하는 과정

### AuthenticationForm ✅✅✅

- 로그인을 위한 built-in form(로그인 창)

    - 로그인하고자 하는 사용자 정보를 입력 받음

    - 기본적으로 username과 password를 받아 데이터가 유효한지 검증

- request를 첫번째 인자로 취함

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)
```

#### login()

- login(request, user, backend=None)

- 인증된 사용자를 로그인 시키는 로직. view 함수에서 사용

    - 입력된 데이터를 판단해서, 현재 세션에 데이터를 입력.

- 현재 세션에 연결하려는 인증된 사용자가 있는 경우 사용

- HttpRequest 객체와 User 객체가 필요

- `auth_login(request, form.get_user())`

#### get_user()

- AuthenticationForm의 인스턴스 메서드

- 유효성 검사를 통과했을 경우 로그인한 사용자 객체를 반환

### Authentication with User

- 현재 로그인 되어있는 유저 정보 출력하기

- 템플릿에서 인증 관련 데이터를 출력하는 방법 => `{{ user }}`

- 어떻게 base 템플릿에서 context 데이터 없이 user 변수를 사용할 수 있을까?

- **settings.py의 context processor 설정 값** 때문

    - **템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록**

    - 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨

    - 즉 django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해 둔 것

    - 현재 user 변수를 담당하는 프로세서는 django.contrib.auth.context_processors.auth

    - 더 많은 빌트인 컨텍스트 프로세서는 검색

    - **현재 로그인한 사용자를 나타내는 User 클래스의 인스턴스가 템플릿 변수 {{user}}에 저장**

    - **로그인하지 않은 경우 AnonymousUser 클래스의 인스턴스로 생성**

## Log out ✅✅✅

- 유저 삭제가 아니라

- **Session을 DELETE**하는 과정

- 서버와 클라 둘 다 지워준다.

### logout(request)

- HttpRequest 객체를 인자로 받고 반환 값이 없음

- 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음

- 2가지 일 처리 ✅

    1. 현재 요청에 대한 sesssion data를 DB에서 삭제 ✅

    2. 클라이언트의 쿠키에서도 sessionid를 삭제 ✅

    - 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스하는 것을 방지하기 위함

```python
# accounts/views.py
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```