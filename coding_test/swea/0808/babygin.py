import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    data = list(map(int, list(input())))

    cnt = [0] * 12
    for i in range(len(data)):
        cnt[data[i]] += 1

    ans = 0
    for i in range(0, len(cnt) - 2):
        if cnt[i] >= 3:
            ans += 1
            cnt[i] -= 3
        if cnt[i] and cnt[i + 1] and cnt[i + 2]:
            ans += 1
            cnt[i] -= 1
            cnt[i + 1] -= 1
            cnt[i + 2] -= 1

    print(f'#{tc} ', end='')
    if ans == 2:
        print(1)
    else:
        print(0)


'''
T = int(input())

for t in range(1, T+1):
    cnt = [0]*10
    dataList = list(map(int, input()))
    for v in dataList:
        cnt[v] += 1

    print(cnt)
'''