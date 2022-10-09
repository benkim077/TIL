# 그리디 알고리즘을 이용해서 풀어봄
# 최적 부분 구조, 탐욕 선택 속성
def solve():
    global N

    ans = 0
    while N > 0:
        if N >= 6:
            ans += min(pkg_cost, a_cost * 6)
            N -= 6
        else:
            ans += min(pkg_cost, a_cost * N)
            N -= N

    return ans


N, M = map(int, input().split())
pkg_cost, a_cost = [0] * M, [0] * M
for i in range(M):
    pkg_cost[i], a_cost[i] = map(int, input().split())

pkg_cost = min(pkg_cost)
a_cost = min(a_cost)

print(solve())




'''
# 두 번째 풀이
# 몫, 나머지를 이용해서 풀이..
# 그리디 알고리즘이 이런 풀이 형태가 많이 나오긴 하는데, 
# 이런 풀이가 그리디 알고리즘 해결법인지는 의문이다.
# 수학을 이용해서 푼 것 같다.

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
pkg_cost, a_cost = [0] * M, [0] * M
for i in range(M):
    pkg_cost[i], a_cost[i] = map(int, input().split())

s, r = N // 6, N % 6
pkg_cost = min(pkg_cost)
a_cost = min(a_cost)

for_s = min(pkg_cost, a_cost * 6) * s
for_r = min(pkg_cost, a_cost * r)

print(for_s + for_r)
'''