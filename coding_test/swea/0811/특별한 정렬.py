import sys
sys.stdin = open('input.txt')


def selection_sort(arr: list, is_asc: bool) -> list:
    arr = [arr[i] for i in range(len(arr))]
    if is_asc:
        for i in range(len(arr) - 1):
            mn = 100
            idx_mn = -1
            for j in range(i, len(arr)):
                if mn > arr[j]:
                    mn = arr[j]
                    idx_mn = j
            arr[i], arr[idx_mn] = arr[idx_mn], arr[i]
        return arr
    else:
        for i in range(len(arr) - 1):
            mx = 0
            idx_mx = -1
            for j in range(i, len(arr)):
                if mx < arr[j]:
                    mx = arr[j]
                    idx_mx = j
            arr[i], arr[idx_mx] = arr[idx_mx], arr[i]
        return arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    lst = list(map(int, input().split()))

    lst_asc = lst_desc = []
    lst_asc = selection_sort(lst, True)
    lst_desc = selection_sort(lst, False)

    print(f'#{tc}', end=' ')
    for i in range(5):
        print(lst_desc[i], end=' ')
        print(lst_asc[i], end=' ')
    print()
