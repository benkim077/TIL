# 중위표기식을 후위표기식으로 변환해주는 함수
def infix_2_postfix(infix_sik: str) -> list:
    stk = []                            # 연산자를 담아두는 스택
    lst = []                            # 리턴할 결과를 담는 리스트
    for char in infix_sik:
        if char == '+':                     # + 일 때
            while stk:                          # 연산자 우선순위가 낮은게 없으니까
                lst.append(stk.pop())           # 스택에 있는 것 다 꺼내서 리스트에 넣는다.
            stk.append(char)                    # +를 스택에 넣는다.
        elif char == '*':                   # * 일 때
            while stk and stk[-1] == '*':       # 스택의 top이 *인 경우에
                lst.append(stk.pop())           # 스택에서 다 꺼내서 리스트에 넣는다
            stk.append(char)                    # *를 스택에 넣는다.
        else:                               # 피연산자일 때
            lst.append(char)                    # 리스트에 넣는다.

    while stk:                          # 스택이 빌 때 까지
        lst.append(stk.pop())               # 스택에 있는 것을 pop해서 리스트에 넣는다.

    return lst                          # 리스트를 리턴한다.


# 후위표기식 계산 결과를 리턴하는 함수
def get_result_postfix(postfix_sik: str) -> int:
    stk = []                            # 피연산자를 담아두는 스택

    for char in postfix_sik:
        if char == '+':                     # + 일 때
            right = stk.pop()
            left = stk.pop()
            stk.append(right + left)            # 스택에서 2번 pop한 값을 더해서 다시 스택에 넣는다.
        elif char == '*':                   # * 일 때
            right = stk.pop()
            left = stk.pop()
            stk.append(right * left)            # 스택에서 2번 pop한 값을 곱해서 다시 스택에 넣는다.
        else:
            stk.append(int(char))           # 피연산자는 숫자로 바꿔서 스택에 넣는다.

    return stk.pop()                    # 계산이 끝나고 스택에 남아있는 값을 리턴한다.


import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())                                # 수식의 길이
    data_infix = input()                            # data_infix는 중위표기식

    data_postfix = infix_2_postfix(data_infix)      # 중위표기식을 후위표기식으로 변환
    ans = get_result_postfix(data_postfix)          # 후위표기식을 계산

    print(f'#{tc} {ans}')                           # 출력
