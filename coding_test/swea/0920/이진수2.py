import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    data = float(input())

    ans = ''
    i = 0
    while True:
        data = data * 2
        if data >= 1:
            ans += '1'
            data -= 1
        else:
            ans += '0'

        if data == 0:
            break

        i += 1
        if i > 12:
            ans = 'overflow'
            break

    print(f'#{tc} {ans}')