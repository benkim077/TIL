# 표준 입출력 방법

## Python 표준 입출력

### 입력

- Raw 값의 입력 : `input()`

    - 받은 입력값을 문자열로 취급

- Evaluated된 값 입력 : `eval(input())`

    - 받은 입력값을 평가된 데이터 형으로 취급

### 출력

- `print()`

    - 표준 출력 함수. 출력값의 마지막에 개행 문자 포함

## 파일의 내용을 표준 입력으로 읽어오는 방법

- `import sys`

- `sys.stdin = open('input.txt', 'r')`

- `sys.stdout = open('output.txt', 'w')`