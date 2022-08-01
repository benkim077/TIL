# Box Model

## CSS 원칙 1

- 모든 요소는 네모(박스모델)이고

- 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.

- 인라인 디렉션은 좌우, 블럭 디렉션은 위아래

## Box Model

- 모든 HTML 요소는 Box 형태로 이뤄짐

- 하나의 박스는 네 부분(영역)으로 이뤄짐

    - Margin 바깥쪽 여백

    - Border 테두리

    - Padding 안쪽 여백

    - Content 실제 내용

- padding, margin shorthand

    - 하나는 전체

    - 2개는 상하/좌우
    
    - 3개는 상/좌우/하
    
    - 4개는 상우하좌

- border shorthand

    - border-width: 2px;

    - border-style: dashed;

    - border-color: black;

    - border: 2px dashed black;

## Box Sizing

- 기본적으로 모든 요소의 box-sizing은 content-box

    - padding을 제외한 순수 content 영역만을 box로 지정

- 우리는 border까지의 너비를 100px로 보는 것을 원함

    - box-sizing을 border-box로 설정