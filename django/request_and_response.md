# 요청과 응답

- URLS -> VIEW -> TEMPLATE 데이터 흐름 이해하기

## URLs


## View

- HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성

- Template에게 HTTP 응답 서식을 맡김

### render()

- `render(request, template_name, context)`

- `settings` 에 `TEMPLATES`에서 

    - `'APP_DIRS': True,` 각 앱의 template 폴더에 있으니까, 알아서 찾아라는 뜻

    - `'DIRS': [],` 리스트에 템플릿들이 들어가는 경로를 추가해줄 수 있다.