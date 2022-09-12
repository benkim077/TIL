# 원형 큐 Circular Queue

## 선형 큐 이용시의 문제점 - 잘못된 포화상태 인식

- 배열의 앞부분에 공간이 있음에도, 포화상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨

> 앞 부분을 활용하고 싶다면 어떻게 해야 할까? => 원형 큐로 해결

## 원형 큐

- 1차원 배열을 사용하지만, 논리적으로 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용

- rear가 n-1까지 갔으면, rear를 다시 맨 앞으로 보낸다.

## 원형 큐 구현

- 초기 공백 상태 front = rear = 0

- 한 칸을 비워두고 계산을 간단하게 하는 방식으로 구현

```
q = [0] * n
front = rear = 0
```

### Index 순환

- front와 rear가 인덱스 n-1을 가리키면, 0으로 이동시킨다.

- 나머지 연산자 mod 사용

### front 인덱스

- 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둔다.

    - 원형 큐는 큐가 가득차는 문제를 해결하는 것은 아니다.

### 원형 큐 삽입 및 삭제 연산

- 삽입 위치 rear = (rear + 1) mod n

```
def enQ(item):
    global rear
    if isFull()
        print('Q_full')
    else
        rear = (rear + 1) % len(q)
        q[rear] = item
```

- 삭제 위치 front = (front + 1) mod n

```
def deQ()
    global front
    if isEmpty()
        print('q empty')
    else:
        front = (front + 1) % n
        return q[front]
```

### 공백상태 및 포화상태 검사

- (rear + 1) mod n == front 일 때, 가득 찬 상태

```
def isFull()
    return (rear + 1) % len(q) == front
```

- front == rear 일 때, 빈 상태

```
def is Empty()
    return front == rear
```