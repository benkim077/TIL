# 에러와 예외

## 문법 에러 Syntax Error

- 문법 에러가 발생하면, 해당 위치 이후 파이썬 프로그램은 실행 되지 않음

- 파일이름, 줄번호 ^ 문자를 통해, 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현. 

    - 줄에서 에러가 발생한 가장 앞 위치를 가리키는 캐럿caret 기호(^)

### 문법 에러 종류

- Invalid syntax 문법 오류

- assign to literal 잘못된 할당

- End of Line(EOL) 괄호

- End of File(EOF) 괄호

## 예외 Exception

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤

    - 문법이 맞더라도 발생하는 에러

- 실행 중 감지되는 에러를 예외라 한다.

- 예외의 여러 타입

    - NameError

    - TypeError 

    - ZeroDivisionError

    - ValueError

    - IndexError

    - KeyError

    - ModuleNotFoundError

    - Import Error

    - KeyboardInterrupt

    - IndentationError

- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐

- 사용자 정의 예외를 만들어 관리할 수 있음

### 파이썬 내장 예외(built-in exception)

계층 구조를 살펴보자. [링크](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy)