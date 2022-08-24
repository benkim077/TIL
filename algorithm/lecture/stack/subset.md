# 부분집합 구하기

- 백트래킹 기법으로 powerset을 구해보자.

- True 또는 False값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용.

- 배열의 i 번째 항목은 i 번쨰 원소가 부분집합의 값인지 아닌지를 나타내는 값이다.

- 이전에 배웠던 loop를 이용한 코드 다시 살펴보기.

## powerset을 구하는 백트래킹 알고리즘

- 후보를 추천하는 부분

- 후보를 가져다가 사용하는 부분

- 이런 형식을 갖추면 기본적으로 백트래킹으로 본다.

- 형식을 만들었을 때의 장점.

    - 기본 틀을 가져다 쓸 수 있다.

    - 후보군을 추천하는 작업과 최종 해를 사용하는 부분은 문제에 맞게 함수를 변형해서 사용하면 된다.

    - 나머지 기본 틀은 그대로 사용

- 

### 부분집합을 만들어보자

### 가지치기 해보자



# 순열

- 항상 메모리, 저장된 값을 기준으로 생각하기

- 나중에 또 나오니까 너무 무리하지 말기

- 크게 3가지 방법 중 1가지를 배운다.

- 나머지도 쉽게 가져다 쓸 수 있다.

## 순열 만드는 알고리즘

- 먼저 넣어 놓고, 가능한 모든 순서로 나열하는 방식

- 0번 결정할 건데, 넣어진 것 그대로 쓸거야

- 모든 자리를 결정하고 오면, 원래 있던 값에서 오른쪽에 있는 얘랑 자리를 바꿔서 다시 만들어볼래.

- 그 다음에는 그 다음 칸이랑 자리를 바꿔볼래

- 이렇게 하면, 각 숫자들이 모두 0번 인덱스에 오게 된다. 

- 코드로는 갔다 온 다음에 원래 상태로 만들어놓고, 그 옆자리랑 바꾸는 방식.

## 활용 예제

- 방문하는 순서가 달라질 때 마다 비용이 달라질 때, 비용을 계산하라.

- 일을 맡는 순서가 달라질 때, 비용을 계산하라.

## 코드

```python

```