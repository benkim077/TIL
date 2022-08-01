# CSS-transition(전환)

효과가 변경되었을 때 부드럽게 처리해주는 CSS의 기능이다. 

## transition 속성

transition-duration : 트랜지션 시간 지정

transition-property : 트랜지션 대상을 설정

transition-delay : 딜레이 설정

transition-timing-function : 트랜지션 중 이동 함수 설정

## event - transitionend

transitionend는 트랜지션을 완료하면 발생하는 이벤트이다. 

### 속성

transitionend 이벤트는 두 속성을 제공한다.

- propertyName : 트랜지션을 완료한 CSS 속성의 이름을 나타내는 문자열

- elapsedTime : 이벤트가 발생한 시점에 해당 트랜지션이 진행된 시간을 초로 나타내는 실수. transition-delay 값에 영향 받지 않는다.

### 사용

addEventListener를 이용해서 이벤트를 사용할 수 있다.

## Reference

[CSS 트랜지션 사용하기 - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions#%EB%A9%94%EB%89%B4_%ED%95%98%EC%9D%B4%EB%9D%BC%EC%9D%B4%ED%8C%85%EC%97%90_%ED%8A%B8%EB%9E%9C%EC%A7%80%EC%85%98_%EC%82%AC%EC%9A%A9)

[전환(transition) - CSS](https://opentutorials.org/module/2367/13691)
