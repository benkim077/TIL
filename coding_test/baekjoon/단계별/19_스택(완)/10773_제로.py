K = int(input())

stk = [0] * K
sp = 0
for _ in range(K):
    num = int(input())
    if num != 0:    # push
        stk[sp] = num
        sp += 1
    else:
        sp -= 1

ans = sum(stk[:sp])
print(ans)