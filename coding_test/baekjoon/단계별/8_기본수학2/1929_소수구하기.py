M, N = map(int, input().split())
data = [i for i in range(M, N + 1)]

ans_lst = []
for num in data:
    if num == 1:
        continue

    i = 2
    while i < num ** 0.5 + 1:
        if num % i == 0:
            break
        i += 1
    else:
        ans_lst.append(num)

for ans in ans_lst:
    print(ans)