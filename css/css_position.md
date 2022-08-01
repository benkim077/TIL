# CSS Position

- 레이아웃을 결정할 떄 사용

- 문서 상에서 요소의 위치를 지정

- 5가지 position property values

- static: 모든 태그의 기본 값(기준 위치)

    - 일반적인 요소의 배치 순서에 따름(좌측 상단)

    - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능

    - relative 상대 위치

        - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)

        - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음

        - 위치 차지. 위치는 그대로 있는데 다른 곳에 있는 것 처럼 보임

    - absolute 절대 위치

        - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow 벗어남)

        - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 브라우저 화면 기준으로 이동)

        - 위치 차지 하지 않음.

    - fixed 고정 위치

        - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow 벗어남)
        
        - 부모 요소와 관계없이 viewport를 기준으로 이동

            - 스크롤 시에도 항상 같은 곳에 위치함

    - sticky 스크롤에 따라 static > fixed로 변경

        - 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성 

CSS 원칙 3

- position으로 위치의 기준을 변경