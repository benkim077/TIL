# The Django authenication system

- 장고 인증 시스템은 인증과 권한부여를 함께 제공(처리)

    - 인증과 권한을 합쳐 인증 시스템이라 한다.

- 필수 구성은 `settings.py > INSTALLED_APPS`에 이미 포함

    - `django.contrib.auth`

- 인증 Authentication

    - 신원 확인

    - 사용자가 자신이 누구인지 확인

- 권한, 허가 Authorization

    - 권한 부여

    - 인증된 사용자가 수행할 수 있는 작업을 결정

    - 장고는 일반적으로 권한을 admin, staff, 일반 사용자로 구분

> 우리는 인증에 집중. 정규 과정에서 권한을 수정하거나 커스텀하는 일은 없다.(advanced)

- 사전 설정

    - **accounts라는 앱**을 만들어서 회원, 인증 관련된 것을 처리.

    - 장고에 auth 관련 키워드를 accounts라는 이름으로 사용하는 경우가 많아서 도움이 된다.

## 커스텀 유저 모델로 대체하는 이유 ✅

- 기본 User Model을 Custom User model로 대체해야 함.

> '왜 기본 유저 모델을 안쓰고, 필수적으로 custom User model로 대체하나?'

- 기본 빌트인 User model의 인증 요구사항이 적절하지 않을 수 있다. ✅

    - username 대신 email을 식별 값으로 쓰고 싶은 경우 등

- 하지만, 프로젝트 도중에 기존 user model을 수정하는 것이 쉽지 않다. ✅

- 대체하기

    - `AUTH_USER_MODEL` 설정 값으로 Defautl User Model을 재정의(override)할 수 있도록 함

### AUTH_USER_MODEL

- AUTH_USER_MODEL은 프로젝트에서 User를 나타낼 때 사용하는 모델

    - 기본값은 auth.User(auth 앱의 User 클래스)

        - INSTALLED_APPS에서 확인할 수 있음

    - (참고) settings.py는 global_settings.py를 상속받아 재정의하는 파일. 그래서 AUTO_USER_MODEL이 settings.py에서 안보이는 것

- 프로젝트가 진행되는 동안 변경할 수 없음

    - 첫 마이그레이션 전에 확정 지어야 하는 값

### 커스텀 유저 모델로 대체하는 방법 ✅

> 3단계, 시험? ✅✅

1. 커스텀 유저 모델 작성

- AbstractUser을 상속받는 User 클래스를 만든다.

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

2. django 프로젝트에서 User를 나타내는데 사용하는 모델을 생성한 커스텀 User 모델로 지정

- `settings.py > AUTH_USER_MODEL = 'accounts.User'` 작성

3. admin.py에 커스텀 User 모델 등록 ✅

- 기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음

```python
# accounts/admin.py
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

#### (참고) Abstract base classes(추상 기본 클래스)

- (결론) DB 테이블로 만들어지지 않는 클래스

- 다른 모델의 기본 클래스로 사용될 경우, 해당 필드가 하위 클래스의 필드에 추가 됨.

- 몇 가지 공통 정보를 다른 모델에 넣을 때 사용하는 클래스(상속용)

#### (주의) 프로젝트 중간에 AUTH_USER_MODEL 변경하기

- 모델 관계에 영향을 미치기 때문에 훨씬 더 어려운 작업이 필요

    - 변경사항이 자동으로 수행될 수 없기 때문

- 프로젝트 처음에 진행하기

#### 데이터베이스 초기화(프로젝트 중간일 경우) (중요)

- 수업 진행을 위한 데이터베이스 초기화 후 마이그레이션

1. migrations 파일 삭제

    - `migrations/` 및 `__init__.py`는 삭제하지 않음

    - 번호가 붙은 파일만 삭제

2. `db.sqlite3` 삭제

3. migrations 진행

    - makemigrations

    - migrate

- 각 앱의 migrations는 서로 유기적인 연결을 가지고 있어 중간에 수정하기 어렵다.

- db의 테이블 이름이 auth_user > accounts_user로 바뀜!

#### User 모델을 반드시 대체해야 할까? ✅

- 기본 User 모델이 충분 하더라도 커스텀 User 모델을 설정하는 것을 강력하게 권장

- 커스텀 유저 모델은 기본 유저 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문 ✅

- User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 마쳐야 함 ✅