import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    st = input()

    stk = [0] * len(st)
    top = -1
    ans = 1
    for i in range(len(st)):
        if st[i] == '(' or st[i] == '{':
            top += 1
            stk[top] = st[i]
        elif st[i] == ')':
            if stk[top] == '(':
                top -= 1
            elif stk[top] == '{':
                ans = 0
                break
            elif top == -1:
                ans = 0
                break
        elif st[i] == '}':
            if stk[top] == '{':
                top -= 1
            elif stk[top] == '(':
                ans = 0
                break
            elif top == -1:
                ans = 0
                break
        else:
            pass

    if top != -1:
        ans = 0

    print(f'#{tc} {ans}')
