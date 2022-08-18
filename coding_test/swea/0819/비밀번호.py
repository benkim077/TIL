import sys
sys.stdin = open('input.txt')

T = 3

for tc in range(1, T + 1):
    N, strg = input().split()
    N = int(N)

    stk = list()
    stk.append(strg[0])
    for i in range(1, N):
        if stk and stk[-1] == strg[i]:
            stk.pop()
        else:
            stk.append(strg[i])

    # for i in range(N):
    #     if i == 0:
    #         stk.append(strg[i])
    #     else:
    #         if stk:
    #             if stk[len(stk) - 1] == strg[i]:
    #                 stk.pop()
    #             else:
    #                 stk.append(strg[i])
    #         else:
    #             stk.append(strg[i])

    ans = ''.join(stk)
    print(f'#{tc} {ans}')
