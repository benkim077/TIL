'''
반복문에 대한 새로운 시야가 틔였다. 물론 스스로 한 것은 아니지만

Q. 반복문의 변수 중에서 어떤 부분이 가장 변하지 말아야 하는가?
이런 질문이 완전 탐색에선 필요없지만, 반복문을 빠져나와야 하는 경우에는 꼭 필요하다.
'''

import sys

sys.stdin = open('input.txt')


def is_palindrome(lst):
    if lst == lst[::-1]:
        return len(lst)
    else:
        return 0


def get_t_arr(lst):
    for i in range(0, 100):
        for j in range(i + 1, 100):
            lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
    return lst


T = 10
for _ in range(1, T + 1):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]

    ans = 0
    mx = 1
    go_out = False
    # 가로 방향 회문 구하기
    for j in range(100, 1, -1):  # 회문 길이
        for i in range(100):  # 행번호
            for s in range(0, 100 - j):  # 시작 위치
                temp = is_palindrome(arr[i][s: s + j])
                if mx < temp:
                    mx = temp
                    go_out = True
                    break
            if go_out:
                break
        if go_out:
            break

    ans = mx

    mx = 1
    go_out = False
    # 세로 방향 회문(전치행렬)
    t_arr = get_t_arr(arr)
    for j in range(100, 1, -1):
        for i in range(100):
            for s in range(0, 100 - j):
                temp = is_palindrome(t_arr[i][s: s + j])
                if mx < temp:
                    mx = temp
                    break
            if go_out:
                break
        if go_out:
            break

    # 어떤 것이 더 큰가?
    if ans < mx:
        ans = mx

    # 출력
    print(f'#{tc} {ans}')
