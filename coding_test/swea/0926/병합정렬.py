def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid_idx = len(lst) // 2
    # left_lst = lst[:mid_idx]
    # right_lst = lst[mid_idx:]

    left_lst = merge_sort(lst[:mid_idx])
    right_lst = merge_sort(lst[mid_idx:])

    return merge(left_lst, right_lst)


def merge(left_lst, right_lst):
    rlt = []

    while len(left_lst) > 0 or len(right_lst) > 0:
        if len(left_lst) > 0 and len(right_lst) > 0:
            if left_lst[0] <= right_lst[0]:
                rlt.append(left_lst.pop(0))
            else:
                rlt.append(right_lst.pop(0))
        elif len(left_lst) > 0:
            rlt.append(left_lst.pop(0))
        elif len(right_lst) > 0:
            rlt.append(right_lst.pop(0))

    return rlt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    sorted_data = merge_sort(data)
    print(sorted_data)

    # print(f'#{tc} {cnt_left} {cnt_right}')