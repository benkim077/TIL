import sys

sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    strg = input()

    stk = [0] * len(strg)
    top = -1
    for i in range(len(strg)):
        # 스택이 비었거나, top이랑 다르면 stk.push(strg[i])
        if top == -1 or stk[top] != strg[i]:
            top += 1
            stk[top] = strg[i]
        # 스택의 top과 같으면 stk.pop()
        elif stk[top] == strg[i]:
            top -= 1

    print(f'#{tc} {len(stk[:top + 1])}')
