import sys
sys.stdin = open('input.txt')


def bin_search(ele, lst, s, e):     # target, lst, start, end
    global cnt, ans
    r_flag = 0
    while s <= e:
        m = (s + e) // 2
        if lst[m] == ele:
            return 1
        elif lst[m] < ele:  # 오른쪽에 있는 경우
            if r_flag == 1:
                return 0
            r_flag = 1
            s = m + 1
        else:               # 왼쪽에 있는 경우
            if r_flag == 2:
                return 0
            r_flag = 2
            e = m - 1
    return 0


    # global cnt, ans
    # if s > e:
    #     return
    # else:
    #     m = (s + e) // 2
    #     if lst[m] == ele:
    #         # if cnt == 0:
    #         #     ans += 1
    #         return
    #     elif lst[m] < ele:
    #         bin_search(ele, lst, m + 1, e)
    #         cnt += 1
    #     elif lst[m] > ele:
    #         bin_search(ele, lst, s, m - 1)
    #         cnt -= 1


T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    A_lst = list(map(int, input().split()))
    A_lst.sort()
    B_lst = list(map(int, input().split()))

    ans = 0
    for ele in B_lst:
        ans += bin_search(ele, A_lst, 0, len(A_lst) - 1)  # ele가 A_lst에 있는지 이진 탐색으로 확인

    print(f'#{tc} {ans}')