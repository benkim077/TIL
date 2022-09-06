# ModelForm

> Model Class, Form Class 중복된 부분이 많아..

> 사용자 입력을 모델과 동일한 필드에 받을거라면, 모델을 기반으로 한 폼을 만들자!

- ModelForm은 모델에 대한 정보를 미리 들고가는 Form이다. 

- ModelForm을 사용하면, Form Class를 일일이 재정의할 필요가 없어진다.

- Model을 통해 Form Class를 만들 수 있는 helper class

- Form과 똑같은 방식으로 View 함수에서 사용한다.

## ModelForm 선언

- forms 라이브러리에서 파생된 ModelForm 클래스를 상속받는 클래스 선언하고, 내부 클래스 Meta를 만든다.

    - model, fields 클래스 변수를 사용한다.

```python
# articles/forms.py
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article         # not Article()
        fields = '__all__'
```

### Meta Class

- 모델 폼에 대한 정보(메타데이터)를 작성하는 곳

- model 속성은 모델폼을 사용할 경우 참조할 Model Class이다.

    - 모델 클래스의 이름만 적어준다. (호출하지 않고 참조)

    - 참조는 대상을 필요한 시점에 사용할 수 있도록 해 준다. 즉, ModelForm이 Model 클래스를 필요한 시점에 사용하기 위한 것이다.

    - 클래스의 경우에는 인스턴스가 필요한 것이 아닌, 클래스의 필드나 속성 등을 내부적으로 참조하기 위한 이유도 있다.

- 참조하는 모델에 정의된 필드 정보를 Form에 적용

- field 속성에 `'__all__'`를 사용하여 모델의 모든 필드를 포함할 수 있음

- exclude 속성을 사용하여 일부 필드를 제외할 수도 있다.

## ModelForm with view funtions

> ModelForm으로 인한 view 함수의 변화를 살펴보자.

- 모델폼을 도입하면 필드의 갯수와 상관없이 하나로 줄어들게 된다.

- 완성된 Model을 기반으로 한 Form에서 받은 데이터이기 때문에, 알아서 모델의 컬럼과 매핑이 된다. request.POST로 한 번에 넘길 수 있다.

### is_valid()

- 유효성 검사 실행, 데이터 유효 여부를 bool 타입으로 반환

- is_valid()의 반환값이 False인 경우 form 인스턴스의 errors 속성에 값이 작성(유효성 검증 실패 원인이 dict 타입으로 저장)

```python
# articles/views.py
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,       # form.error에 실패 원인이 저장
    }
    return render(request, 'articles/new.html', context)
```

- 위 코드를 사용하면, 유효성 검증 실패 시 사용자에게 실패 결과 메세지를 출력해줄 수 있다.

### save() 메서드

- form 인스턴스에 바인딩 된('데이터가 들어간'이라는 뜻) 데이터를 통해 데이터베이스 객체를 만들고 저장

- ModelForm의 하위 클래스(여기서는 ArticleForm)는 **키워드 인자 `instance` 여부**를 통해 생성할 지, 수정할 지를 결정

    - instance가 제공되지 않은 경우, save()는 지정된 모델의 새 인스턴스를 만든다.(CREATE)
    
    - instance가 제공된 경우, save()는 해당 인스턴스를 수정(UPDATE)

        - instance 값으로 수정 대상 객체를 지정

    - (참고) instance는 키워드 인자이므로, 반드시 `instance=` 형태로 사용한다. 맨 처음 ModelForm의 생성자 함수의 맨 처음 인자는 data이므로, `data=`를 생략할 수 있었다.

## Form과 ModelForm

> 시험?

- 둘은 각자 역할이 다르다.

- 공통점 : 사용자의 요청을 받아서 처리하는 것

- Form

    - 사용자로부터 받는 데이터가 DB와 연관되어 있지 않은 경우

    - DB에 영향을 미치지 않고 단순 데이터만 사용되는 경우

- ModelForm

    - 사용자로부터 받는 데이터가 DB와 연관되어 있는 경우에 사용

    - 데이터 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 매핑해야 할 지 이미 알고 있기 때문에 곧바로 save() 호출이 가능

## 위젯 활용하기

- 완성된 인스턴스만 템플릿에 출력되다 보니까 인스턴스를 만들어주는 폼클래스 객체를 조작.

```python
# articles/forms.py
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목'
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        ),
    )

    class Meta:
        model = Article
        fields = '__all__'
```