# Templates

> 주의
>
> 경로 `/index/`와 `index/`의 차이점

## DTL Django Template Language


### Variable

`{{variable}}` 변수를 통해 view에서 넘겨준 context를 template에서 접근할 수 있다.

### Filter

- 들어온 값을 조작하고 싶을 때 사용

- `{{variable|filter_name}}`

### Tags

- 여러 기능(반복, 논리 등)

- `{% tag %}`

### Comments

- 주석

## Template Inheritance 상속

- 코드의 재사용성

- `{% extends '' %}`

- `{% block content %}{% endblock content %}`