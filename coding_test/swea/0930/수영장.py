import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    day, month, three_m, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    i = 1
    while i < 13:
        if plan[i] * day > month:
            plan[i] = month
        else:
            plan[i] *= day
        i += 1

    i = 3
    while i < 13:
        if plan[i] + plan[i - 1] + plan[i - 2] > three_m:
            plan[i], plan[i - 1], plan[i - 2] = 0, 0, 0
            plan[i - 2] = three_m
            i += 3
            continue
        i += 1

    if sum(plan) > year:
        ans = year
    else:
        ans = sum(plan)

    print(f'#{tc} {ans}')