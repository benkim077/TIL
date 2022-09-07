# authentication with user

- User Object와 User CRUD에 대한 이해

- 회원 가입, 회원 탈퇴, 회원정보 수정, 비밀번호 변경

## 회원 가입

- 회원가입은 User를 CREATE 하는 것. 

- UserCreationForm built-in form을 사용

### UserCreationForm

- 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm

- 3개의 필드를 가짐

    1. username(from the user model)

    2. password1

    3. password2

## Custom user & Built-in auth forms

- AbstractBaseUser의 모든 subclass와 호환되는 forms

    - 아래 Form 클래스는 User 모델을 대체하더라도 커스텀 하지 않아도 사용 가능

        1. 

        2. 

        3. 

        4. 

    - 기존 User 모델을참조하는 Form이 아니기 때문

- 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms

    1. UserCreationForm - 회원가입

    2. UserChangeForm - 정보수정

- 두 form 모두 class Meta: model = User가 등록된 form이기 때문에 반드시 커스텀(확장)해야 함

###  커스텀 하기

- UserCreationForm()

- UserChangeForm()

- get_user_model으로 모델을 간접 호출


#### get_user_model()

- 현재 프로젝트에서 활성화된 사용자 모델(active  usermodel)을 반환

- 직접 참조하지 않는 이유

    - User 모델을 커스텀한 상황에서는 커스텀 User 모델을 자동으로 반환해주기 때문

- django는 User 클래스는 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 강조

- 자세한 내용은 추후 보충

## 회원 탈퇴

- DB에서 유저를 DELETE 하는 것

## 회원 정보 수정

- User를 UPDATE 하는 것

- UserChangeForm built-in form을 사용

### UserChangeForm

- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm

- ModelForm이기 때문에 instance 인자로 기존 user 데이터 정보를 받는 구조 동일함

- CustomUserChangeForm으로 확장했었기 때문에, 이걸 사용함.

### 비밀번호 변경

- 사용자가 비밀번호를 변경할 수 있도록 하는 Form

- 이전 비밀번호를 입력하여 비밀번호를 변경

- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스

#### PasswordChangeForm



# Limiting access to logged-in users

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

