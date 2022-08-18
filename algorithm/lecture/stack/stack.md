# 스택

- 선형 자료 구조

> 선형 자료 구조(1:1 관계), 비선형 구조(N:M 관계, 트리 등)

- 후입선출(LIFO)

## 스택 구현

### 자료구조

- 자료를 선형으로 저장할 저장소가 필요

    - 배열(lst)

    - top: 마지막으로 삽입된 원소의 위치(stack pointer; SP)

### 연산

- lst.append() 또는 lst.pop()

> lst의 append, pop 메소드는 느리다. 
> (배열이 계속 생성되는 방식이기 때문)
>
> 그럴 땐, 필요한 길이 만큼 0으로 초기화된 stack을 만들고, top 변수를 sp로 활용한다.

#### push: 스택에 자료 삽입

- stk.append() 메소드

- push A

    ```
    top++
    if top == size, overflow
    else stk[top] = A
    ```

#### pop: 삭제. 삽입한 자료의 역순으로 꺼낸다.

- stk.pop() 메소드

- pop

    ```
    top--
    if top == -1, underflow
    else return stk[top + 1]
    ```

#### 기타 연산

- isEmpty: 스택이 비었는지 확인

- peek: top의 item을 반환

### 스택 구현 고려 사항

- 스택을 구현하는 방법 2가지

> 알고리즘 문제풀이에선 1번 방법 사용

- 1차원 배열

    - 구현이 쉽지만, 스택 크기 변경이 어렵다.

- 동적 연결 리스트

    - 구현이 어렵지만 메모리를 효율적으로 사용한다.

## 스택 활용 예시

### 괄호

### 함수 호출