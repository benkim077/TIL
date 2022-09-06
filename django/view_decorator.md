# View Decorators

- 데코레이터를 이용해서 view 함수 강화하기

    - 데코레이터 : 기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 추가해주는 함수

## Allowed HTTP methods

- django.views.decorators.http의 데코레이터를 사용하여 요청 메서드를 기반으로 접근을 제한할 수 있다.

- 일치하지 않는 메서드 요청이라면 405 반환

    - 405 Method Not Allowed : 요청 방법이 서버에게 전달 되었으나 사용 불가능한 상태

```python
# views.py
from django.views.decorators.http import require_http_methods, require_safe, require_POST
```

- `@require_safe()` require_GET이 있지만, require_safe를 권장

- `@require_http_methods(['GET', 'POST'])` view 함수가 특정한 요청 method만 허용하도록 하는 데코레이터

- `@require_POST` view 함수가 POST 요청 메서드만 허용하도록 하는 데코레이터