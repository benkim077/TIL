# HTML 문서 구조화

## 인라인/블록 요소

- HTML 요소는 크게 인라인/블록 요소로 나눔

- 인라인 요소는 글자처럼 취급

- 블록 요소는 한 줄 모두 사용

## 텍스트 요소

- `<a>` href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성

- `<b>`, `<strong>` 굵게

- `<i>`, `<em>` 기울이기

- `<br>` 줄 바꿈

- `<img>` src 속성을 활용하여 이미지 표현

- `<span>` 의미 없는 인라인 컨테이너

## 그룹 컨텐츠

- `<p>` 하나의 문단(paragraph)

- `<hr>` 문단 레벨 요소에서의 주제의 분리를 의미. 수평선으로 표현됨

- `<ol>` 순서가 있는 리스트

- `<ul>` 순서가 없는 리스트

- `<pre>` HTML에 작성한 내용을 그대로 표현. 보통 고정폭 글꼴이 사용되고 공백문자를 유지

- `<blockquote>` 텍스트가 긴 인용문. 주로 들여쓰기를 한 것으로 표현

- `<div>` 의미 없는 블록 레벨 컨테이너

### form

- 정보(Data)를 서버에 제출하기 위해 사용하는 태그

- `<form>` 기본 속성

    - action : form을 처리할 서버의 URL

    - method : form을 제출할 때 사용할 HTTP 메서드(get 혹은 post)

        - get : URL에 입력값이 표시됨

        - post : 암호화? 숨김?

    - enctype : method가 post인 경우 데이터의 유형

        - application/x-www-form-urlencoded : 기본값

        - multipart/form-data : 파일 전송시(input type이 file인 경우)

        - text/plain : HTML5 디버깅 용(잘 사용되지 않은)

### input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공된다.

- 대표 속성

    - name : form control에 적용되는 이름(이름/값 페어)

        form 안에 입력받는 곳이 input

    - value : form control에 적용되는 값

    - required, readonly, autofocus, autocomplete, disabled

### input label

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음

    - 상호작용 영역 증가

    - label과 input의 관계 설정

- input에 대한 상세한 설명

- input에 id 속성, labal에 for 속성을 활용하여 상호 연관 시킴

### input 유형 - 일반

- 일반적으로 입력을 받기 위해 제공되며 타입별로 HTML 기본 검증 혹은 추가 속성을 활용할 수 있음

    - text : 일반 텍스트 입력

    - password : 입력 시 값이 보이지 않고 문자를 *로 표현

    - email : 이메일 형식이 아닌 경우 form 제출 불가

    - number : min, max, step 속성을 활용하여 숫자 범위 설정 가능

    - file : accept 속성을 활용하여 파일 타입 지정 가능

### input 유형 - 항목 중 선택

- 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함

- 동일 항목에 대해서는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함

    - checkbox : 다중 선택

    - radio : 단일 선택

### input 유형 - 기타

- 다양한 종류의 input을 위한 picker를 제공

    - color : color picker

    - date : date picker

- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정

    - hidden : 사용자에게 보이지 않는 input

### select

드랍다운 선택 만들기

```html
<div>
    <label for="region">지역을 선택해주세요.</label><br>
    <select name="region" id="region" required>
        <option value="">선택</option>
        <option value="서울">서울</option>
        <option value="대전">대전</option>
        <option value="광주">광주</option>
    </select>
</div>
```

라디오 버튼 만들기

```html
<div>
    <p>OS를 선택해주세요.</p>
    <input type="radio" name="OS" id="Windows" value="Windows" checked>
    <label for="Windows">윈도우</label><br>
    <input type="radio" name="OS" id="MacOS" value="MacOS">
    <label for="MacOS">맥</label><br>
</div>
```