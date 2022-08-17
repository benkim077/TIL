import sys

sys.stdin = open('input.txt', encoding='UTF-8')

T = 10

for tc in range(1, T + 1):
    _ = int(input())
    word = input()
    st = input()

    ans = 0

    for i in range(len(st) - len(word) + 1):
        for j in range(len(word)):
            if word[j] != st[i + j]:
                break
            if j == len(word) - 1:
                ans += 1

    print(f'#{tc} {ans}')
