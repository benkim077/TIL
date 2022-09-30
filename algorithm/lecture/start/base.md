# 진수

## 진수 변환

### 10진수 -> 타 진수로 변환

- 원하는 진법의 수로 나눈 뒤 나머지를 거꾸로 읽는다.

### 타 진수 -> 10진수로 변환

### 2진수, 8진수, 16진수간 변환

- 3자리, 4자리씩 묶음 또는 나열

### 컴퓨터에서 음의 정수 표현 방법

- 1의 보수 : 부호와 절대값으로 표현된 값을 부호 비트를 제외한 나머지 비트들을 0은 1로, 1은 0으로 변환한다.

    - -6 : 11111111 - 00000110 = 11111001

    - 보수의 맨 앞이 1이면 음수(부호 비트)

- 2의 보수 : 1의 보수방법으로 표현된 값의 최하위 비트에 1을 더한다.

    - -6 : 11111010 : 2의 보수 표현

    - 6과 -6을 더하면 (1)00000000이 된다. 