# Closure
> **배경**
Local scope에서 global scope에 접근하는 것은 가능하다.
그러나 중첩된 함수에서 둘러싼 함수에 접근하는 것은 불가능하다.
그것을 가능하게 만드는 것이 클로저이다.

> **목적**
[Excute context](./execute_context.md)를 바탕으로, JS closure에 대해 이해한다.

## Dynamic Scope and Static Scope

어디에서 **호출**했느냐에 따라, 접근할 수 있는 유효범위가 달라진다는 것을 **dynamic scope**라 한다. 
반면에 함수의 **선언** 위치에 따라, scope가 달라지는 것을 **static scope**(**lexical scope**)라 한다.
**JS의 scope는 static scope**를 따른다.

## Nested function and Closure

**중첩 함수**(**Nested Function**)란 함수 내부에 정의된 함수이다.
중첩 함수(자식 함수)의 execute context에서, **부모 함수가 closure**가 된다.
이 때, 중첩 함수의 scope chain은 local > closure > script > global이다.
**자식 함수는 closure scope를 통해, 자신이 정의된 부모 함수와 scope에 접근할 수 있다.**

## Example Code

```js
// Closure를 활용하는 방법1 - 함수 공장(Function Factory)
// fontSize를 바꾸는 버튼을 만들어주는 함수, 를 만들어주는 makeSizer 함수
function makeSizer(size) {
  return function() {
    document.body.style.fontSize = size + 'px';
  };
}

var size12 = makeSizer(12);
var size14 = makeSizer(14);
var size16 = makeSizer(16);
```

## Reference

[생활코딩 - closure](https://youtu.be/bwwaSwf7vkE)
[Su Bak - 스코프란?](https://medium.com/@su_bak/javascript-%EC%8A%A4%EC%BD%94%ED%94%84-scope-%EB%9E%80-bc761cba1023)
[Su Bak - Lexical Scope(Static) and Dynamic Scope](https://medium.com/@su_bak/javascript-lexical-scope-static-scope-and-dynamic-scope-c4a9e941fab3)
[mdn - closures](https://developer.mozilla.org/ko/docs/Web/JavaScript/Closures)