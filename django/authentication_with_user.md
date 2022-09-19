# authentication with user

> 계속해서 Built-in form을 사용해서, 회원가입, 회원관리, 회원탈퇴 등을 학습

- User Object와 User CRUD에 대한 이해

- 회원 가입, 회원 탈퇴, 회원정보 수정, 비밀번호 변경

## 회원 가입

- 회원가입은 User를 CREATE 하는 것. 

- `UserCreationForm` built-in form을 사용

### UserCreationForm

- 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm

- 3개의 필드를 가짐

    1. username(from the user model)

    2. password1

    3. password2

```python
# Custom으로 대체한 코드
# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .form import CustomUserCreationForm, CustomUserChangeForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

## Custom user & Built-in auth forms ✅

- AbstractBaseUser의 모든 subclass와 호환되는 forms

    - 아래 Form 클래스는 User 모델을 대체하더라도 커스텀 하지 않아도 사용 가능

        1. AuthenticationForm

        2. SetPasswordForm

        3. PasswordChangeForm

        4. AdminPasswordChangeForm

    - 기존 User 모델을참조하는 Form이 아니기 때문

- 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms ✅

    1. UserCreationForm - 회원가입

    2. UserChangeForm - 정보수정

- 두 form 모두 class Meta: model = User가 등록된 form이기 때문에 반드시 커스텀(확장)해야 함

### 커스텀 하기

- UserCreationForm()

- UserChangeForm()

- get_user_model으로 모델을 간접 호출

```python
#accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
```

#### get_user_model()

- **현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환**

- 직접 참조하지 않는 이유

    - User 모델을 커스텀한 상황에서는 커스텀 User 모델을 자동으로 반환해주기 때문

- django는 User 클래스는 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 강조

- 자세한 내용은 추후 보충

## 회원 탈퇴

- DB에서 유저를 DELETE 하는 것

```python
# accounts/views.py
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')
```

- **탈퇴 후 로그아웃** 순서. 

    - 먼저 로그아웃하면 해당 요청 객체 정보가 없어지기 때문

## 회원 정보 수정

- User를 UPDATE 하는 것

- `UserChangeForm` built-in form을 사용

### UserChangeForm

- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm

- ModelForm이기 때문에 instance 인자로 기존 user 데이터 정보를 받는 구조 동일함

- CustomUserChangeForm으로 확장했었기 때문에, 이걸 사용함.

#### UserChangeForm 사용 시 문제점

- 일반 사용자가 접근해선 안 될 정보들(fields)까지 모두 수정이 가능해짐

- admin 인터페이스에서 사용되는 ModelForm이기 때문

- 따라서 CustomUserChangeForm에서 접근가능한 필드를 조정해야 함.

- 수정하고자 하는 필드 작성

```python
# accounts/forms.py
class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
```

```python
# accounts/views.py
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instace=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```

### 비밀번호 변경

- 사용자가 비밀번호를 변경할 수 있도록 하는 built in form `PasswordChangeForm`

- 이전 비밀번호를 입력하여 비밀번호를 변경

- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스

```python
# accounts/views.py
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

#### 암호 변경 시 세션 무효화 방지하기

- 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 로그인 상태가 유지되지 못함.

- `update_session_auth_hash(request, user)`

- 현재 요청과 새 세션 데이터가 파생될 업데이트된 사용ㅈ아 객체를 가져오고, 세션 데이터를 적절하게 업데이트 해준다.

- `form.save()`밑에 `update_session_auth_hash(request, form.user)` 추가
