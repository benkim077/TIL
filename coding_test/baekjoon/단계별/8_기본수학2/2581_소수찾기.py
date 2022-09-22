M = int(input())
N = int(input())
data = [i for i in range(M, N + 1)]

is_found_first = False
sm = 0
mn_v = 100
for num in data:
    if num == 1:
        continue

    i = 2
    while i < num:
        if num % i == 0:
            break
        i += 1
    else:
        if not is_found_first:
            mn_v = num
            is_found_first = True
        sm += num

if not is_found_first:
    print(-1)
else:
    print(sm)
    print(mn_v)