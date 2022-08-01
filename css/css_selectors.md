# CSS Selectors

수 많은 요소 중 선택한다.

## 선택자 유형

- 전체 선택자 `*`

- 요소 선택자 `tag_name`

    - HTML 태그를 직접 선택

- 클래스 선택자 `.class_name`

    - 해당 클래스가 적용된 항목을 선택

- 아이디 선택자 `#id_name`

    - 해당 아이디가 적용된 항목을 선택

    - 단일 id를 권장

 속성 선택자

- 결합자(Combinators)

    - 자손 결합자 `selector1 selector2`

        s1 안에있는 s2

    - 자식 결합자 `selector > selector`

    - 일반 형제 결합자
    
    - 인접 형제 결합자

- 의사 클래스/요소(Pseudo Class)

    - 링크, 동적 의사 클래스

    - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

## 적용 우선순위 (cascading order)

- 범위가 좁을 수록 강하다.

- CSS 우선 순위를 아래와 같이 그룹 지을 수 있다.

    - 중요도

        - !important

        - 주의

    - 우선순위

        inline - id - class, 속성, ...

    - CSS 파일 로딩 순서

## CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.

    - 속성 중에는 상속이 되는 것과 되지 않는 것들이 있다.

    - 되는 것

        - text 관련 요소, opacity, visibility

    - 상속 안되는 것

        - 여백, 레이아웃

        - Box model 관련 요소, Position 관련 요소