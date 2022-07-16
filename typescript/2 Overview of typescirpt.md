# 2 Overview of Typescript

# 2.0 How Typescript Works

JS는 개발자의 실수를 도와주지 않는다.

```tsx
function divide(a, b){
    return a/b
}

divide("hello")
```

이런 코드를 타입스크립트는 미리 알려준다.

# 2.1 Implicit Types vs Explicit Types

## TS의 타입 시스템에 대해서

JS를 하다 왔다면 어떤 타입인지 지정하지 않아도 됐다. C는 모든 것의 타입을 정해줘야 한다. JAVA 같은 곳에서는 매우 명시적이어야 한다.

TS는 두 가지를 결합했다.

명시적으로 정의할 수도 있고, 아니면 그냥 JS처럼 변수만 생성하고 넘어가도 된다.

좋은 점은 TS가 타입을 추론해준다는 점이다.

```tsx
let a = "hello"
// 이것만으로 a의 타입이 추론된다.
// a 는 string
a = "bye"
// 가능
a = 1
//이건 JS에서는 완전히 가능하다. 하지만 TS에선 아니다.
// 이렇게 하면 버그가 될 수 있다. 그래서 안된다.
```

```tsx
//좀 더 구체적으로, 명시적으로
let b : boolean = "x"
// TS의 문법. 이게 진짜 TS이다.
// Type Checker 와 소통하는 방식
// 이런 식으로 명확하게 알려줄 수 있다.
// boolean을 string으로 했다. 에러.
let b : boolean = false
//이런 식으로 작성한다.
//이렇게 하지 않는 것을 추천한다.

let c = [1,2,3]
c.push("1")
//string을 넣으려고 하는 것이기 때문에 작동하지 않는다. JS에선 가능하다.

let c : number[] = []
//명시적 표현
```

명시적 표현은 최소한으로 사용한다. TS가 추론하게 하는게 더 낫다.

# 2.2 Types of TS part One

기본적인 TS의 타입 외의 다른 타입을 알아본다.

지금까지 number, string, boolean, 각 타입의 array 등의 type을 배웠다.

이것들은 basic type 이었다.

## 이제 optional type을 알아보자.

### optional type

```tsx
const player : {
    name: string,
    age?: number //optional
} = {
    name: "nico"
}

if(player.age && player.age < 10){

}
```

### Alias type

```tsx
type Player = {
    name: string,
    age?: number
}

const nico : Player = {
    name: "nico"
}
const lynn : Player = {
    name: "lynn",
    age: 12
}
```

### function argument & return type

```tsx
type Player = {
    name: string,
    age?: number
}

function makePlayer(name:string) : Player{
    return {
        name:name
    }
}

const nico = makePlayer("nico")
nico.age = 12
```

### arrow function

```tsx
const makePlayer = (name:string) : Player => ({name})
```

# 2.3 Types of TS part Two

더 많은 타입을 알아보자.

### read-only

```tsx
type Player = {
    readonly name: string
    age?: number
}

function makePlayer(name:string) : Player{
    return {
        name:name
    }
}

const nico = makePlayer("nico")
nico.age = 12

nico.name = "las"
```

```tsx
const numbers: readonly number[] = [1,2,3,4]
numbers.push(1)//에러
```

filter, map 등은 가능. 이는 배열을 바꾸지 않기 때문.

Object는 여기까지

## 이제 Tuple을 알아보자

Tuple은 순서가 있는 배열을 얻었을 때 활용한다.

```tsx
const player: readonly [string, number, boolean] = ["nico", 12, true]
player[0] = 1//error, string && readonly
player[0] = "hi" //error
```

## null, undefined

```tsx
let a : undefined = undefined
let b : null = null
```

## Any

어떤 타입이든 될 수 있다. 바보처럼 TS를 사용하고 싶을 때.

any를 쓰면 TS를 빠져나오는 것. 보호장치를 잃게 된다.

사용하지 않는 것을 추천.

```tsx
let a  = []
```

```tsx
const a : any[] = [1,2,3,4]
const b : any = true

a + b //not error
```

# 2.4 Types of TS part Three

Typescript의 중요한 점은 Type Checker와 소통하는 것

내가 코드를 설명해주면, TS가 바보 같은 짓을 할 때 보호해주는 것이다.

## unknown

어떤 타입인지 모르는 변수는 어떻게 해야 할까?

어떤 작업을 할 때 확인해야 하는 방식으로 보호해준다.

```tsx
let a : unknown

if(typeof a === 'number'){
    let b = a + 1
}

if(typeof a === "string"){
    let b = a.toUpperCase()
}
```

## void

아무것도 리턴하지 않는 함수를 대상으로 사용한다.

```tsx
//void 함수
function hello():void{
    console.log('x')
}
```

void를 굳이 써줄 필요는 없다. 써줄 수도 있다.

## never

함수가 절대 return하지 않을 때 발생한다.

```tsx
function hello(name:string|number):never{
    if(typeof name === "string"){
        name //name is string
    } else if(typeof name === "number"){
        name //name is number
    } else {
        name // never. 절대 실행되면 안되는 코드.
    }
}
```


