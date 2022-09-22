N = int(input())
data = list(map(int, input().split()))

ans = 0
for num in data:
    if num == 1:
        continue

    i = 2
    while i < num:
        if num % i == 0:
            break
        i += 1
    else:
        ans += 1

print(ans)