import sys
sys.stdin = open('input.txt')


def solve(short, long):
    mx = -300
    for i in range(len(long) - len(short) + 1):
        temp = 0
        for j in range(len(short)):
            temp += short[j] * long[i:i + len(short)][j]
        if temp > mx:
            mx = temp
    return mx


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A_data = list(map(int, input().split()))
    B_data = list(map(int, input().split()))

    if len(A_data) >= len(B_data):      # A가 더 길거나 같은 경우
        ans = solve(B_data, A_data)
    else:                               # A가 더 짧은 경우
        ans = solve(A_data, B_data)

    print(f'#{tc} {ans}')
