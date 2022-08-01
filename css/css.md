# CSS

- Cascading Style Sheets

- 계단식, 상속, 퍼져나가는

- 스타일을 지정하기 위한 언어

    - 속성으로 HTML 태그를 선택하고, 스타일을 지정한다.

## CSS 구문

```CSS
h1 { /*선택자*/
  color: blue; /*선언*/
  font-size: 15px; /*속성: 값*/
}
```

모든 h1 태그에 내가 지정한 스타일이 적용된다.

- 선택자를 통해 스타일을 지정할 HTML 요소를 선택

- 속성(property), 값(value)

## CSS 정의 방법

### 인라인(inline)

- 태그에 직접 style 속성을 활용

### 내부 참조(embedding) 

- head에서 `<style>`에 작성한다.

### 외부 참조(link file)

- 분리된 CSS 파일

- head에서 `<link>`로 파일을 링크시킨다.

- 가장 많이 쓰는 방식

### 선택자의 우선순위

- 우선순위가 있다~

## CSS 개발자 도구

- styles : 해당 요소에 선언된 모든 CSS

- computed : 해당 요소에 최종 계산된 CSS