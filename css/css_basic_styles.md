# CSS 기본 스타일

## 크기 단위

- px(픽셀)

    - 모니터 해상도의 한 화소인 '픽셀' 기준

    - 픽셀의 크기는 변하지 않기 때문에 고정적 단위

- %

    - 백분율 단위

    - 가변적 레이아웃에서 자주 사용

- em

    - (바로 위, 부모 요소에 대한) 상속의 영향을 받음

    - 배수 단위, 요소에 지정된 사이즈에 상대적 사이즈를 가짐

- **rem**

    - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음

    - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

        - 브라우저 기본 글자 기준(16px)

    em 보다 rem을 많이 씀.

## 크기 단위(viewport)

- 웹페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)

- 내가 보고있는 화면의 크기 전체를 의미한다.

- 디바이스의 viewport를 기준으로 상대적 사이즈가 결정됨

- vw, vh, vmin, vmax

    - 1vh, 1vw는 viewport / 100 이다.

    - vmin, vmax 최소, 최대 범위. 마찬가지로 100분의 1단위

    - 항상 내가 보는 화면에 꽉 차는 정사각형을 만들고 싶다면,

## 색상 단위

- 색상 키워드(background-color: red;)

    - 대소문자 구별 X

- RGB 색상(background-color: rgba(0, 255, 0, 0.5);)

## CSS 문서 표현

- 텍스트

    - font-size

    - 서체(font-family)

    - 서체 스타일(font-style, font-weight)

    - 자간(letter-spacing)

    - 단어 간격(word-spacing)

    - 행간(line-height)

        - `line-height: 50%;`를 통해 수직 정렬을 할 수 있다. 

- 컬러(color)

- 배경(background-image, background-color)

- 기타 HTML 태그별 스타일링

    - 목록(li)

    - 표(table)