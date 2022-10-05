# 댓글Comments - 게시물Article 관계 (N:1)

- 0개 이상의 댓글은 1개 게시글에 작성될 수 있음

## Comment 모델 정의

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```



```python
# shell_plus
article = Article.objects.create(title='title', content='content')  # 게시물 생성

comment = Comment()
comment.article = article   # article 객체 자체를 넣어준다.
comment.content = 'first comment'
comment.save()
```



### admin site 등록

- 새로 작성한 Comment 모델을 admin site에 등록

```python
# articles/admin.py

from .models import Article, Comment

admin.site.register(Comment)
```

## Comment 구현

- 외래키 필드를 출력에서 제외

```python
# articles/forms.py
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('article',)
```

- 출력에서 제외된 외래키는 variable routing을 사용(url을 통해 변수를 넘김)

```python
# articles/urls.py

urlpatterns = [
    ...,
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
```

```python
# articles/views.py

def comments_create(request, pk):
    article = Article.object.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```

#### save() method

- commit=False 옵션

- 아직 DB에 저장되지 않은 인스턴스를 반환

- 저장하기 전에 객체에 대한 처리를 수행할 때 사용

### Read 구현

- 작성한 댓글 목록 출력하기

```python
# articles/views.py

def detail(request, pk):
    ...
    comments = article.comment_set.all()
    context = {
        ...
        'comments': commetns,
    }
    ...
```

- detail 템플릿에서 for문을 사용해서 댓글 목록 출력

### DELETE 구현

```python
# articles/urls.py

urlpatterns = [
    ...,
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
```

```python
# articles/views.py

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.object.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

```html
<!-- articles/detail.html -->
...
<form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
    csrf
    input submit
</form>
```

### Comment 추가 사항

1. 댓글 개수 출력하기

    - DTL filter - length 사용

        - `{{ comments|length }}` 또는 `{{ article.comment_set.all|length }}`

    - Queryset API - count() 사용

        - `{{ comments.count }}` 또는 `{{ article.comment_set.count }}`

2. 댓글이 없는 경우 대체 컨텐츠 출력하기

    - for 에서 `{% empty %}`를 추가

# Article - User N:1 관계

- Article(N) - User(1)

- Article 모델과 User 모델 간 관계 설정

- 0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음

## Referencing the User model

- 유저 모델과의 관계에서 신경써야 할 것에 대해서.

- 장고에서 유저 모델을 참조하는 방법

    1. settings.AUTH_USER_MODEL

    2. get_user_model()

### settings.AUTH_USER_MODEL

- 반환 값: 'accounts.User' (문자열)

- User 모델에 대한 외래 키 또는 M:N 관계를 정의할 때 사용

- models.py 모델 필드에서 User 모델을 참조할 때 사용

### get_user_model()

- 반환 값 : User Object(객체)

- models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용
