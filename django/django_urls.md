# Django URLs

> 웹 앱은 URL을 통한 클라이언트의 요청에서 시작

## Trailing URL Slashes

> URL 끝에 '/'를 붙일 것인가?

- django는 붙여주는 것이 디폴트

    - 이를 **URL 정규화**라 함

    - 복수의 페이지에서 같은 컨텐츠가 존재하는 것을 방지

## Variable routing 작성

> 비슷한 URL과 Template을 계속 만들어야 하나? => variable routing

- URL **주소 일부를 변수 지정**하여 **view 함수의 인자**로 사용

- 변수는 `<type:name>`으로 정의한다.

- 변수의 기본 타입은 str. 5가지 타입(str, int, slug, uuid, path)

## App URL Mapping

> 앱이 많아졌을 때 urls.py를 각 app에 매핑하는 방법

- `project/urls.py`에서 모든 `path()`를 관리하지 않는다.

- `app/urls.py`로 URL 매핑을 위탁한다.

```python
# pjt/urls.py
from django.urls import path, include

urlpatterns = [
    # ...
    path('app1/', include('app1.urls'))
    path('app2/', include('app2.urls'))
]
```

### include()

> **URL configuration**이란? URL path와 views function을 매핑해주는 모듈.

- include()는 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 돕는 함수

- 남은 문자열 후속 처리를 include된 URLconf로 전달

## Naming URL patterns의 필요성

- 링크에 URL을 직접 작성하지 말고, **path()에서 name 인자를 정의**해서 사용

- **DTL URL 태그**로 path()에서 작성한 name을 사용할 수 있다.

> url 태그에서 사용하던 것이 path의 name 속성에서 온 것이구나!