# CSS Layout

## CSS layout techniques

- display

- position

- float

- flexbox

- grid

- 기타

    - Responsive Web Design, Media Queries

## Float

### CSS 원칙 1

- Normal Flow

    - 좌측 최상단 부터 쌓인다.

    - inline은 글자

    - block은 한 줄씩

- 모든 요소는 네모(박스모델)

### float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜, 텍스트를 포함한 **인라인 요소들이 주변**을 감싸도록 함

- 요소가 Normal flow를 벗어나도록 함

- float left, float right

- (참고) box 모델끼리는 겹치게 되므로 clear: both 를 통해 초기화를 했었다. 지금은 안씀.

### float 속성

- none : 기본값

- left : 요소를 왼쪽으로 띄움

- right : 요소를 오른쪽으로 띄움

- float의 한계(어려웠던 점)

    - 수직 정렬

    - 아이템의 너비와 높이 혹은 간격을 동일하게 배치

> 결국엔 왼쪽, 오른쪽으로 치워버리는 것 만 된다.

## Flexbox

- 행과 열 형태로 아이템들을 배치하는 레이아웃 모델

    (참고)z-index라는 것도 있다.

- 구성 요소

    - Flex Container(부모 요소)

    - Flex Item(자식 요소)

- flex container(부모 요소)에 `display: flex;`

    - flex items(자식 요소. 컨테이너 안에 있는 요소들)가 inline처럼 변경된다.

- 축

    - main axis(메인 축)

        - 꼬치 꼽는 축

    - cross axis(교차 축)

        - 뜯어 먹는 축

- `display: inline-flex`

    - 안에 있는 요소들 만큼만 크기를 차지하게 된다.

    - **inline 속성은 주변 요소들에 영향받는다고 이해하자.**

## flexbox 속성

### flex 속성 구분

#### container에 적용하는 속성

- display

- flex-direction

- flex-wrap

- flex-flow

- justify-content

- align-items

- align-content

#### items에 적용하는 속성

- flex-basis

- flex-grow

- flex-shrink

- flex

- align-self

- order

- z-index

### 배치 관련 속성들

> flex-direction과 flex-wrap

#### flex-direction

> main 축 방향을 설정하는 것. 배치 방향 설정

- `flex-direction: row(기본값) row-reverse, column, column-reverse;`

- main axis 기준 방향 설정

- items 나열 순서를 바꿔준다.

#### flex-wrap

> 줄넘김 처리 설정

- `flex-wrap: wrap(줄바꿈), nowrap(줄여서 한 줄에 다 배치. 삐저나감), wrap-reverse(wrap인데, 밑에서부터 쌓인다.)`

- 아이템이 컨테이너를 벗어나는 경우 어떻게 처리할 것인가?

- 기본적으로 컨테이너 영역을 벗어나지 않도록 함

- 어떻게 사용할까?

    - 줄바꿈 하고 싶으면 wrap(기본)

    - 넘치면 그냥 빠져나감 컨테이너를 삐저나감 nowrap

    - 역순으로 배치(최신 글이 위에 오게 하고 싶다면) wrap-reverse

#### flex-flow

- flex-direction과 flex-wrap의 shorthand

- `flex-flow: row nowrap;`

### 공간 배분 (정렬)

> flex-direction에서 정해진 축 방향을 바탕으로 축 위에서 어디에 놓고 싶은가?

#### justify-content(main axis)

- main axis 기준 공간 설정

- item 순서는 변하지 않고, 어디에 배치할 것인지 선택하는 것

- `justify-content: flex-start(왼쪽에), flex-end(오른쪽에), center(가운데 모아서), space-between(items 사이 공간 균등하게), space-around(items의 양옆에 겹치지 않는 공간 하나씩), space-evenly(item 양옆에 겹치는 공간 하나씩)`

#### align-content(cross axis)

- cross axis를 기준으로 공간 배분

- **2줄 이상 되었을 때** cross axis 기준으로 공간 설정

- `align-content: flex-start, flex-end, center, space-between, space-around, space-evenly`

### 정렬

> 아이템 배치 디자인 설정하기

#### align-items

> align-content 랑 비슷하네..

- 모든 아이템을 cross axix 기준으로

- stretch : 쭉 늘림

- flex-start : 위에 붙임

- flex-end : 아래

- center : 가운데

- baseline : 텍스트 baseline에 기준선

#### align-self(개별 아이템)

- 개별 아이템은 cross axis 기준으로 정렬

- 개별 아이템에 적용하는 속성

- stretch

- flex-start

- flex-end

- center

### 기타 속성

- flex-grow : 남은 영역을 아이템에 분배

- order : 배치 순서 바꾸기