# Admin Site

> django 관리자 페이지. automatic admin interface

- `python manage.py createsuperuser` 관리자 계정 생성

- `admin/`로 접속 후 로그인

## 모델의 record를 보기 위해서

```python
# appnames/admin.py
from django.contrib import admin
from .models import Class_name

admin.site.register(Class_name)
```