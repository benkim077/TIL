import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    str1 = list(set(input()))
    str2 = input()

    mx = 0
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1

        if mx < cnt:
            mx = cnt

    print(f'#{tc} {mx}')
