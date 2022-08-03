# CSS Display

## CSS 원칙 2

- display에 따라 크기와 배치가 달라진다.

## 인라인/블럭 요소

- display: block

    - 줄 바꿈이 일어나는 요소

    - 화면 크기 전체의 가로 폭을 차지. 한 줄을 다 차지

    - 차지할 수 있는 너비의 100%를 차지한다.

    - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.

    - width를 주면, 나머지 영역은 자동으로 margin이 된다.

- display: inline

    - 줄 바꿈이 일어나지 않는 행의 일부 요소. 글자처럼 취급

    - content 너비만큼 영역을 차지한다. 자기 자리만 차지

    - width, height, margin-top, margin-bottom을 지정할 수 없다.

    - 상하 여백은 line-height로 지정한다. 

## 블록 레벨 요소와 인라인 레벨 요소

> * 자주쓰는거

블록 레벨 요소

- div *

- ul, ol, li

- p *

- hr *

- form *

등

인라인 레벨 요소

- span *

- a *

- img *

- input, label *

- b, em, i *, strong

등

## inline? 요소 수평 정렬

- 왼쪽 정렬

    - margin-right: auto; 
    
    - text-align:left; 
    
        - **블럭 요소에만 적용 가능.**

        - **블럭 안에 있는 inline에 적용된다.**

- 오른쪽 정렬

    - margin-left: auto;

    - text-align: right;

- 가운데 정렬

    - margin-right:auto; margin-left: auto; 

    - text-align: center;

### inline-block, none

display: inline-block

- block과 inline 레벨 요소의 특징을 모두 가짐

- inline처럼 한 줄에 표시할 수 있고, block 처럼 width, height, margin 속성을 모두 지정할 수 있음

display: none (시험)

- 코드에 있는데 element로 생성조차 되지 않는다. 

- 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

- visibility: hidden은 DOM 트리에 생성 됨. 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.

