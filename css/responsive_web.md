# Responsive Web

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

- 중요 ✔️

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