import sys
sys.stdin = open('input.txt')


def change_to_bin(h_num):
    st = ''
    while h_num > 1:
        st = str(h_num % 2) + st
        h_num //= 2
    st = str(h_num) + st

    while len(st) < 4:
        st = '0' + st

    return st


T = int(input())
for tc in range(1, T + 1):
    N, data = input().split()
    N = int(N)

    bin_data = ''
    ans = ''
    for char in data:
        if ord(char) >= ord('A'):
            temp = 10 + ord(char) - ord('A')
            ans += change_to_bin(temp)
        else:
            ans += change_to_bin(int(char))

    print(f'#{tc} {ans}')
