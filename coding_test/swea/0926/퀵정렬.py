# import sys
# sys.stdin = open('input.txt')


# def qsort(lst, s, e):
#     if s >= e:
#         return lst

#     key = s
#     i, j = s + 1, e

#     while i <= j:
#         while i <= e and lst[i] <= lst[key]:
#             i += 1
#         while j > s and lst[j] >= lst[key]:
#             j -= 1
#         if i > j:
#             lst[j], lst[key] = lst[key], lst[j]
#         else:
#             lst[i], lst[j] = lst[j], lst[i]

#     qsort(lst, s, j - 1)
#     qsort(lst, j + 1, e)
def qsort(lst, s, e):
    if s >= e:
        return lst
    
    key = s
    i, j = s + 1, e

    while i <= j:
        while i <= e and lst[i] <= lst[key]:
            i += 1
        while j > s and lst[j] >= lst[key]:
            j -= 1
        if i > j:
            lst[j], lst[key] = lst[key], lst[j]
        else:
            lst[i], lst[j] = lst[j], lst[i]
    
    qsort(lst, s, j - 1)
    qsort(lst, j + 1, e)



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    qsort(data, 0, N - 1)
    print(data)
    # print(f'#{tc} {data[N//2]}')