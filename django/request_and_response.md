# 요청과 응답 Request and Response

> URL > VIEW > TEMPLATE 데이터 흐름 이해하기

> 이 부분은 MTV 구조 흐름과 연결해서 학습하기

## URLs

- `project_name/urls.py`

- URL들을 적절한 View로 **분배**한다.(우편 배달부)

## View

- `app_name_s/views.py`

- **HTTP 요청을 수신하고 HTTP 응답을 반환**하는 함수 작성

- Template에게 HTTP 응답 서식을 맡김

### render() 함수

- 템플릿을 컨텍스트와 결합하고 렌더링 된 텍스트와 함께 **HttpResponse 객체를 반환**하는 함수

- `render(request, template_name, context)`

    - `request` 요청 객체

    - `template_name` 템플릿의 전체 이름 또는 경로

    - `context` 템플릿에서 사용할 데이터(dict type)

## Templates

- `app_name_s/templates/template_name.html`

- 실제 내용을 보여주는데 사용되는 파일

### template 경로 설정

- `settings.py > TEMPLATES`에서, 

    - `'APP_DIRS': True,` 템플릿이 각 앱의 template 폴더에 있고 알아서 찾아준다.

    - `'DIRS': [],` 템플릿들이 들어가는 경로를 추가해줄 수 있다.