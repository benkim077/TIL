import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    day_p, month_p, three_p, year_p = map(int, input().split())
    data = [0] + list(map(int, input().split()))



'''
T = int(input())
for tc in range(1, T + 1):
    day_p, month_p, three_p, year_p = map(int, input().split())
    data = [0] + list(map(int, input().split()))

    ans_lst = [0] * 13
    for i in range(1, 13):
        ans_lst[i] = min(data[i] * day_p, month_p) + ans_lst[i - 1]

        if i > 2:
            ans_lst[i] = min(ans_lst[i], three_p + ans_lst[i - 3])
    ans = min(ans_lst[-1], year_p)

    print(f'#{tc} {ans}')
'''