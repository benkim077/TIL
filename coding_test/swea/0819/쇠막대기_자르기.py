T = int(input())
for tc in range(1, T + 1):
    strg = input()

    stk = []
    ans = 0
    for i in range(len(strg)):
        if strg[i] == '(':
            stk.append('(')
        else:
            if strg[i - 1] == '(':
                stk.pop()
                ans += len(stk)
            else:
                stk.pop()
                ans += 1

    print(f'#{tc} {ans}')