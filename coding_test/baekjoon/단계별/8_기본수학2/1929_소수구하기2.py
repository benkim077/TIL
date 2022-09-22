def get_prime_lst(s, n):
    check = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if check[i] == True:
            for j in range(i + i, n, i):
                check[j] = False
    
    return [i for i in range(s, n) if check[i] == True]


M, N = map(int, input().split())

ans_lst = get_prime_lst(M, N)
for num in ans_lst:
    print(num)