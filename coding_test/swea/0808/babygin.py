T = int(input())

for t in range(1, T+1):
    cnt = [0]*10
    dataList = list(map(int, input()))
    for v in dataList:
        cnt[v] += 1

    print(cnt)