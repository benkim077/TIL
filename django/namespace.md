# 네임스페이스

- 다른 앱에 동일한 이름의 URL이 있는 경우에 문제 발생

    1. 현재 앱의 URL로 이동하는 문제

    2. 이동해도 기존 앱의 URL 템플릿이 출력되는 경우

- URL 네임스페이스와, template 네임스페이스로 해결한다.

## URL namespace

- **URL namespace**를 사용하면, 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용할 수 있음.

- 각 앱의 urls.py에 urlpatterns 위에 `app_name = '앱_이름'`을 적어준다.

- **이제 URL tag를 사용할 때 `{% url 'app_name:url_name' %}` 형태를 사용**하자.

> (추가) NoReverseMatchError => URL 태그를 확인하자

## Template namespace

> 다른 앱으로 이동은 됐지만, 여전히 기존 앱의 템플릿이 출력되는 경우 => **Template namespace**로 해결하자.

- `app_name/templates/`에 있는 파일을 찾을 수 있는 것이 디폴트 설정이다. 

    - template 이름이 겹치는 경우는 `settings.py > INSTALLED_APPS`에 등록된 순서에 따라서 결정된다.

- **해결 방법** : 샌드위치 구조를 사용한다.

    - views에서 templates 호출 경로를 `app_name/template_name.html`로 바꿔주면 된다.

    - 폴더 구조도 `app_name/templates/app_name/template_name.html`로 바꿔준다.