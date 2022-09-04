# Templates

- HTML 정적 부분과 동적 컨텐츠를 삽입한다.

## DTL (Django Template Language)

### Variable

- `{{var_name}}`

- 변수를 통해 view에서 넘겨준 context(dict type)를 template에서 접근할 수 있다.

### Filter

- `{{var_name|filter_name}}`

- 변수를 조작하고 싶을 때 사용

- filter는 다양하니까 검색해서 필요할 때 마다 검색해서 사용해보기

### Tags

- `{% tag_name %}`

- 여러 기능(반복, 논리 등)

### Comments

- `{# a_comment #}` 

- `{% comment %} lines_of_comment {% endcomment %}`

## Template Inheritance 상속

- `{% extends 'base.html' %}`

    - `base.html`을 상속

- `{% block content %}{% endblock content %}`

    - 이 부분을 제외하고 `base.html`의 내용과 같다.

### 템플릿 경로 추가

- base.html은 `프로젝트 최상단 / templates /`에 위치시킨다.

- `settings.py > TEMPLATES DIRS`에 `'BASE_DIR / 'templates''`를 추가한다.

> BASE_DIR은 프로젝트 최상단을 가리키는 경로 객체