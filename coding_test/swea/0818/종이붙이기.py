import sys

sys.stdin = open('input.txt')


def dp(num):
    cnt = 1
    while cnt <= num:
        if cnt < 3:
            pass
        else:
            if table[cnt] == 0:
                table[cnt] = 1 * table[cnt - 1] + 2 * table[cnt - 2]
            else:
                pass
        cnt += 1


table = [0] * 31
table[1] = 1
table[2] = 3
dp(30)

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) // 10

    print(f'#{tc} {table[N]}')
