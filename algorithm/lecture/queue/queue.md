# 큐 Queue

## 큐의 특성

- 큐의 뒤(tail, rear)에서 삽입, 앞(head, front)에서 삭제

    - rear는 마지막 삽입 위치

    - front는 마지막 삭제 위치

- 선형 자료구조

- 선입선출구조(FIFO: First In First Out)

## 큐의 기본 연산 및 구현

- 1차원 배열을 이용한 큐

- front, rear 두 개의 인덱스

    - front : 저장된 첫 번째 원소의 인덱스

    - rear : 저장된 마지막 원소의 인덱스

- 초기 상태 : front = rear = -1

- 공백 상태 : front == rear

- 포화 상태 : rear == n - 1 (배열의 크기 n)

### createQueue() 공백상태 큐 생성

```
Q = []
front, rear = -1, -1
```

```
q = [0] * n
front, rear = -1, -1
```

### enQueue(item) 삽입

```
rear++
Q[rear] = item
```

```
def enQ(item):
    global rear
    if isFull() : print('Q_full')
    else:
        rear++
        q[rear] = item
```

### deQueue() 삭제

```
front++
```

```
def deQ()
    global front
    if isEmpty(): print('q_empty')
    else:
        front++
        return q[front]
```

### isEmpty() 공백상태 검사

```
if: front == rear
    True
```

```
def isEmpty()
    return front == rear
```

### isFull() 포화상태 검사

```
if: rear == n - 1   # 배열의 크기 n
    True
```

```
def isFull()
    return rear == len(q) - 1
```

### Qpeek() 검색

- front에서 원소를 삭제 없이 반환

- 가장 앞에 있는 원소를 검색하여 반환하는 연산

- 현재 front + 1에 있는 원소를 반환

```
def Qpeek()
    if isEmpty(): print('q_empty')
    else: return q[front + 1]
```