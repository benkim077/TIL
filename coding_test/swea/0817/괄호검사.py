'''
스택을 활용한 기본적인 괄호 문제.
아직 스택에 익숙해지지 못했다.

언제 push? 언제 pop?

pop과 if stk 짝을 맞추자.

문제가 생기는 경우
1. pop stk empty
2. 종료 후 stk 데이터 있는지 있음
'''

import sys

sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    data = list(input())
    stk = list()

    ans = 1
    for i in range(len(data)):
        if data[i] == '(':
            stk.append(data[i])
        else:
            if stk:
                stk.pop()
            else:
                ans = 0
                break
    if stk:
        ans = 0

    print(f'#{tc} {ans}')


