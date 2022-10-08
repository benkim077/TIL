N = int(input())
data = list(map(int, input().split()))

ans = 0
sm = sum(data)
for s in range(N - 1):  # 시작위치 s
    sm -= data[s]           # 나머지 위치의 합
    ans += data[s] * sm     # 곱한 결과를 ans에 더해준다.

print(ans)

'''
시간초과
N = int(input())
data = list(map(int, input().split()))

ans = 0
s = 0
while s < N:
    for j in range(s + 1, N):
        ans += data[s] * data[j]
    s += 1

print(ans)
'''

'''
시간초과

def combination(k, s, value):
    global ans

    if k == r:
        ans += value
        return

    for i in range(N):
        if i >= s and not vsted[i]:
            vsted[i] = True
            combination(k + 1, i + 1, value * data[i])
            vsted[i] = False


N = int(input())
data = list(map(int, input().split()))

r = 2
ans = 0
vsted = [False] * N
combination(0, 0, 1)

print(ans)
'''