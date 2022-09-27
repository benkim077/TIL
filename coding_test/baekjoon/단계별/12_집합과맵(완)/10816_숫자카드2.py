N = int(input())    # 가지고 있는 카드
data_N = list(map(int, input().split()))
M = int(input())    # 비교할 숫자 목록
data_M = list(map(int, input().split()))

cnt_lst_plus = [0] * 10_000_001
cnt_lst_minus = [0] * 10_000_001
cnt_lst_zero = 0

for num in data_N:
    if num < 0:
        cnt_lst_minus[num * (-1)] += 1
    elif num > 0:
        cnt_lst_plus[num] += 1
    else:
        cnt_lst_zero += 1

ans = []
for num in data_M:
    if num < 0:
        ans.append(cnt_lst_minus[num * (-1)])
    elif num > 0:
        ans.append(cnt_lst_plus[num])
    else:
        ans.append(cnt_lst_zero)

print(*ans)