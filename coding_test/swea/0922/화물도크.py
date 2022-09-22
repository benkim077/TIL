import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = []
    for _ in range(N):
        data.append(tuple(map(int, input().split())))

    data.sort(key=lambda x:x[1])

    ans = 1
    e = data.pop(0)[1]
    while data:
        cs, ce = data.pop(0)
        if cs < e:
            pass
        else:
            ans += 1
            e = ce

    print(f'#{tc} {ans}')