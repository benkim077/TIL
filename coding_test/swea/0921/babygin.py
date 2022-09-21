import sys
sys.stdin = open('input.txt')


def bt(k, lst, prev):
    global ans
    if k == 3:
        remainder_lst = []
        for i in range(6):
            if i not in lst:
                remainder_lst.append(i)
        if check(lst) and check(remainder_lst):
            ans = 1
        return

    for i in range(prev + 1, 4 + k):
    # for i in range(6):
        if not vsted[i]:
            vsted[i] = True
            bt(k + 1, lst + [i], i)
            vsted[i] = False


def check(lst):
    if data[lst[0]] == data[lst[1]] == data[lst[2]]:
        return True

    lst.sort()
    if data[lst[0]] + 1 == data[lst[1]] and data[lst[1]] + 1 == data[lst[2]]:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, input()))

    # 0 ~ 5 중에 3개를 선택하는 경우의 수
    ans = 0
    vsted = [False] * 6
    bt(0, [], -1)

    print(f'#{tc} {ans}')

