# Responsive Web

> 가장 인기있는 프론트엔드 오픈 소스. (프레임워크)

## 부트스트랩

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

    - 

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

        - 중첩해서 넣지 마라. Top-level에 둬라. body랑 같은 레벨...?

    - flexbox

    - card - grid card

## Responsive Web Design ✔️

- 반응형 웹 디자인

    - 반응형 웹 만들기 위해서 사용하는 다양한 기술들 중 하나가 그리드 시스템.

### grid system

- layout - grid

- 요소들의 디자인과 배치에 도움을 주는 시스템

- 기본 요소

    - column : 실제 컨텐츠를 포함하는 부분

    - gutter: 칼럼과 칼럼 사이의 공간

    - container : column들을 담고 있는 공간

### Bootstrap grid System ✔️

- Bootstrap Grid system은 flexbox로 제작됨

- container, rows, column으로 컨텐츠를 배치하고 정렬

- 중요

    - grid는 12개의 column

    - 6개의 grid breakpoints

### Grid System Breakpoints

- xs, sm, md, lg, xl, xxl

- breakpoint를 통해서 화면 크게에 따라 반응형 웹을 만든다.

### 연습

- 총 12칸 확인!

```html
    div.row
        div.col <!--절반-->
        div.col <!--절반-->

    div.row
    div.col-3 <!--12칸 중 3칸 먹는다는 의미-->
```

- breaking point 연습. 크기에 따라서 비율이 변경되도록 설정

```html
    h2 grid breakpoint
    div.box.col-2.col-sm-8.col-md-4.col-lg-5 <!--화면 크기에 따라서 달라지는 반응형 grid -->
    div.box.col-8.col-sm-2.col-md-4.col-lg-2
    div.box.col-2.col-sm-2.col-md-4.col-lg-5
```

### offset, nesting 

- nesting 중첩

```html
div.row
    div.box.col-6
        div.row
            div.box col-3
            div.box col-3
            div.box col-3
            div.box col-3
    div.box.col-6
        div.row
            div.box col-6
            div.box col-6
```html

- offset

    - offset만큼 비울 수 있다.

```html
div.row
    div.box.offset-2.col-4  offset-2/col4
    div.box.col-md-4 offset-4   col-md-4/offset-4
```

---

![참고](./images/Screenshot%202022-08-03%20161712.png)

- a 와 img 둘 다 inline 일때, 공간을 넣는 방법