def b_sort(lst, a, b):
    global ans
    if b - a == 1:
        return [lst[a]]
    A = b_sort(lst, a, (a + b) // 2)
    B = b_sort(lst, (a + b) // 2, b)
    if A[-1] > B[-1]:
        ans += 1
    sort_lst = [0] * (len(A) + len(B))
    a = A.pop()
    b = B.pop()
    i = 0
    while True:
        i += 1
        if a < b:
            sort_lst[-i] = b
            if not B:
                while A:
                    i += 1
                    sort_lst[-i] = a
                    a = A.pop()
                sort_lst[0] = a
                return sort_lst
            b = B.pop()
        else:
            sort_lst[-i] = a
            if not A:
                while B:
                    i += 1
                    sort_lst[-i] = b
                    b = B.pop()
                sort_lst[0] = b
                return sort_lst
            a = A.pop()

T = int(input())
for t in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    ans = 0
    print(f'#{t} {b_sort(L, 0, N)[N//2]} {ans}')
