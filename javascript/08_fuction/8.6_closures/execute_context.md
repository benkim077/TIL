# Excute Context
> **목적**
실행 컨텍스트, 콜스택, 스코프에 대해 이해한다.
웹 브라우저 개발자 도구를 이용해서, 실행 컨텍스트에 따라 변수가 어떤 scope에 저장되는지 살펴본다.
(source > debugger > scope, call stack)

## Scope

JS는 변수를 읽을 때, scope에서 찾는다. 
scope에는 local, script, global scope가 있다.
local > script > global 순서로 탐색한다. 셋의 연결을 scope chain이라 한다. global은 항상 접근 가능하다.

```js
// 어떤 변수 키워드를 사용하느냐에 따라, 각각 다른 scope에 저장된다.
// 전역 스코프에서
n0='n0';
var v0='v0';
let l0='l0';
const c0 = 'c0';
```

## Call Stack

excute context가 call stack에 쌓인다.
- global excute context
- function excute context

어떤 execute context에 있는가에 따라, 
- 변수가 저장되는 scope가 달라진다.
- 접근할 수 있는 변수가 달라진다.

```js
// excute context가 바뀌면서, 변수가 어떤 scope에 위치하는지 바뀐다.

// excute context가 fn2(자식 함수)
function fn2(){
    n2='n2';
    var v2='v2';
    // console.log(v1); // 오류
    let l2='l2'; 
    // console.log(l1); // 오류
    const c2='c2;';
    // console.log(c1); // 오류
}

//excute context가 fn1(부모 함수)
function fn1(){
    n1='n1';
    var v1='v1';
    let l1='l1';
    const c1='c1';
    fn2();
}
fn1();
```
## Reference
[생활코딩 - execute context](https://youtu.be/QtOF0uMBy7k)