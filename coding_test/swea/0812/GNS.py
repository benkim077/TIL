import sys

sys.stdin = open('input.txt')

eng_lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())

for tc in range(1, T+1):
    tc_num, N = input().split()
    N = int(N)
    lst = list(input().split())

    ans = []

    for i in range(len(eng_lst)):
        for j in range(N):
            if lst[j] == eng_lst[i]:
                ans += [eng_lst[i]]

    print(tc_num)
    for i in range(len(ans)):
        print(ans[i], end=' ')
    print()
