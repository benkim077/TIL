def get_prime_lst(n):
    check = [True] * (n + 1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if check[i] == True:
            for j in range(i + i, n + 1, i):
                check[j] = False
    
    return [i for i in range(2, n + 1) if check[i] == True]


M, N = map(int, input().split())

ans_lst = get_prime_lst(N)
for i in range(len(ans_lst)):
    if ans_lst[i] >= M:
        ans_lst = ans_lst[i:]
        break

for num in ans_lst:
    print(num)