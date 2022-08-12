import sys

sys.stdin = open('input.txt')

num_lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())

for tc in range(1, T+1):
    tc_num, N = tuple(map(int, input().split()))
    lst = list(map(int, input().split()))

    ans_lst = []

    for i in range(N):
        if num_lst[i] == lst[i]:
            ans_lst += [lst[i]]

    print(ans_lst)