import sys
sys.stdin = open('input.txt')


# 후위표기식 계산 결과를 리턴하는 함수
def get_result_postfix(postfix_sik: str) -> int:
    stk = []

    for char in postfix_sik:
        if char == '+':
            right = stk.pop()
            left = stk.pop()
            stk.append(right + left)
        elif char == '*':
            right = stk.pop()
            left = stk.pop()
            stk.append(right * left)
        else:
            stk.append(int(char))

    return stk.pop()


# table
icp = {'*': 2, '+': 1, '(': 3}
isp = {'*': 2, '+': 1, '(': 0}

T = 10
for tc in range(1, T + 1):
    N = int(input())
    data = input()

    stk = []
    lst = []
    for char in data:
        if char.isdigit():
            lst.append(int(char))
        else:
            if not stk:
                stk.append(char)
            else:
                if char == ')':
                    while stk and stk[-1] != '(':
                        lst.append(stk.pop())
                    stk.pop()
                elif isp[stk[-1]] < icp[char]:
                    stk.append(char)
                else:
                    while isp[stk[-1]] >= icp[char]:
                        lst.append(stk.pop())
                    stk.append(char)

    while stk:
        lst.append(stk.pop())

    ans = get_result_postfix(lst)

    print(f'#{tc} {ans}')
