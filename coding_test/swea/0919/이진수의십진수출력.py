import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, input()))
    N = len(data) // 7
    ans = []
    for n in range(N):
        sm = 0
        for i in range(7):
            sm += data[n * 7 + i] * 2**(6 - i)
        ans.append(sm)
    print(f'#{tc}', *ans)