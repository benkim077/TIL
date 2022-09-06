# Django Form

- 사용자의 **입력 데이터**의 **유효성 검증**이 반드시 필요하다.

- Form은 Django의 **유효성 검사 도구** 중 하나

- Django는 Form을 통해 간단하게, 자동으로 유효성 검사를 할 수 있는 기능을 제공한다.

- Form이 처리해주는 세 부분

    1. 렌더링을 위한 데이터 준비 및 재구성

    2. 데이터에 대한 HTML forms 생성

    3. 클라이언트로부터 받은 데이터 수신 및 처리

## Django Form Class

### Form Class 선언

> Model Class 선언과 비슷함

```python
# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

- forms 라이브러리의 Form 클래스를 상속받는다.

- TextField는 존재하지 않는다.

### 코드 수정

```python
# new view 함수
from .forms import ArticlceForm

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

```html
# new template 업데이트
# ...
# label, input 태그를 지우고,
{{ form.as_p }}
# ...
```

> 코드를 수정한 후 출력을 확인해보자.

- ArticleForm의 인스턴스(form) 하나로 input과 label 태그가 모두 렌더링 된다!

- 각 태그의 속성값도 자동으로 설정됐다. 

#### Form rendering options

- label, input 쌍에 대한 3가지 출력 옵션

1. `as_p()` 각 필드가 p태그로 감싸져서 렌더링

2. `as_ul()` 각 필드가 li태그로 감싸져서 렌더링

3. `as_table()` 각 필드가 tr태그로 감싸져서 렌더링

### Django의 2가지 HTML input 요소 표현

1. Form fields

    - **입력에 대한 유효성 검사** 로직 처리

    - 템플릿에서 직접 사용

2. Widgets

    - 웹페이지의 HTML input 요소 **렌더링**을 담당

    - Widgets은 반드시 form field에 할당

## Widgets

- Django의 HTML input element의 표현을 담당

- 단순히 HTML 렌더링만 처리. 유효성 검증과 관계 없음

- `content = forms.CharField(widget=forms.Textarea)`

> 다양한 built-in 위젯 확인하기

> form field, widgets 공식문서를 찾아보며, 어떻게 조합해서 사용할 수 있는지 찾아보기.


## (추가)Rendering fields manually

- `{{ form.as_p }}` 를 쪼개보자

- django form > working with forms doc > working with form templates > rendering fields manually 를 참고

- 여러가지 방법이 있음. 각각 장단이 있다. 다시보기 참고