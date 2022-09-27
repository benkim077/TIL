import sys
sys.stdin = open('input.txt')


def check_rt(lst):
    cnt_lst = [0] * 12
    for num in lst:
        cnt_lst[num] += 1
    # print(cnt_lst)

    for i in range(10):
        if cnt_lst[i] >= 3:
            return True
        elif cnt_lst[i] >= 1 and cnt_lst[i + 1] >= 1 and cnt_lst[i + 2] >= 1:
            return True
        else:
            continue

    return False


T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    p1_data = [data[i] for i in range(12) if i % 2 == 0]
    p2_data = [data[i] for i in range(12) if i % 2 == 1]
    # print(p1_data, p2_data)

    ans = -1
    for i in range(3, 7):
        p1_flag = check_rt(p1_data[:i])
        p2_flag = check_rt(p2_data[:i])
        # print(p1_data[:i], p2_data[:i])
        # print(p1_flag, p2_flag)
        if p1_flag == True and p2_flag == True:
            ans = 1
            break
        elif p1_flag == True and p2_flag == False:
            ans = 1
            break
        elif p1_flag == False and p2_flag == True:
            ans = 2
            break
        else:
            continue
    else:
        ans = 0

    print(f'#{tc} {ans}')