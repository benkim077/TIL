# CSS Framework

## 부트스트랩

> 가장 인기있는 프론트엔드 오픈 소스. (프레임워크)

- CSS 스타일에는 정형화된 Form들이 있다.

- 이런 것들을 모아서 쓰기 편하게 만들어 둔 것이 bootstrap

- 반응형 웹도 만들 수 있다.

    - 웹페이지의 크기에 따라 변하는 반응형 웹

### CDN

- Content Delivery(Distribution) Network

- 설치하는 게 아니라, 네트워크로 받아서 쓰는 것

## docs

bootstrap docs를 보면서 사용하자.

## spacing

- 마진, 패딩 설정

- `{property}{sides}-{size}`

    - mt-3는 `margin-top: 1rem;`

    - m-1은 `margin: 0.25rem;`

    - mx-auto는 수평 중앙 정렬

    - py-0은 위 아래 padding 0;

|   | sides |
| --- | --- |
| t | top |
| b | bottom |
| s | left |
| e | right |
| x | left, right |
| y | top, bottom |

## color

- `bg-primary` 백그라운드 컬러

- `text-danger` 텍스트 컬러

## Text

- text-start

- text-center

- text-end

- text-decoration-none

- fw-bold

- fst-italic

## Display

- d-inline

### Breakpoint

- 화면 크기에 따라 display 설정 하는 것

- d-sm-none

## Position

- fixed-top

- fixed-bottom

- position-static, absolute

## Components

- bootstrap의 다양한 UI 요소를 활용할 수 있음

> docs 활용하세요

- 기본 제공된 components를 변환해서 활용

    - buttons

    - dropdowns

    - forms > form controls

    - navbar

    - carousel 캐러셀

    - modal

        - 중첩해서 넣지 마라. Top-level에 둬라. (body랑 같은 레벨)

    - flexbox

    - card - grid card