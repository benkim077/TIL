# Admin Site

> django 관리자 페이지. automatic admin interface

- `python manage.py createsuperuser` 관리자 계정 생성

- `admin/`로 접속 후 로그인

## admin에 모델 클래스 등록

- admin 페이지에서 CRUD를 할 수 있다!

```python
# app_name_s/admin.py

from django.contrib import admin
from .models import Class_name

admin.site.register(Class_name)
```