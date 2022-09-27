from collections import deque
import sys

# sys.stdin = open('input.txt')


T = int(input())
for _ in range(T):
    p = input()
    N = int(input())
    data_st = input()

    if len(data_st) == 2 and 'D' in p:
        print('error')
        continue

    if N == 0:
        print(data_st)
        continue

    data_lst = deque(map(int, data_st[1:-1].split(',')))
    # data_lst = deque([])
    # prev = 1
    # for i in range(2, len(data_st)):
    #     if data_st[i] == ',' or data_st[i] == ']':
    #         data_lst.append(int(data_st[prev:i]))
    #         prev = i + 1

    is_reverse = False
    for cmd in p:
        if cmd == 'R':
            is_reverse = bool(is_reverse - 1)
        elif cmd == 'D':
            if not data_lst:
                print('error')
                break
            if is_reverse == False:
                data_lst.popleft()
            else:
                data_lst.pop()
    else:
        print('[', end='')
        if is_reverse == True:
            data_lst.reverse()
        for i in range(len(data_lst)):
            print(data_lst[i], end='')
            if i != len(data_lst) - 1:
                print(',', end='')
        print(']')