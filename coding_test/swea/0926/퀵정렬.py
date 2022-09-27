import sys
sys.stdin = open('input.txt')


def qsort(lst, s, e):
    if s >= e:
        return

    key = s
    i = s + 1
    j = e

    while i <= j:
        while i <= e and data[i] <= data[key]:
            i += 1
        while j > s and data[j] >= data[key]:
            j -= 1
        if i > j:
            data[j], data[key] = data[key], data[j]
        else:
            data[i], data[j] = data[j], data[i]

    qsort(lst, s, j - 1)
    qsort(lst, j + 1, e)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    qsort(data, 0, N - 1)
    # print(data)
    print(f'#{tc} {data[N//2]}')