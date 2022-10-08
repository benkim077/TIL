import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
first_v = int(input())
others = []
for _ in range(N - 1):
    heappush(others, -int(input())) # 최대 힙을 만들어준다.

cnt = 0
while True:
    if len(others) == 0:
        break

    mx = -heappop(others)

    if first_v > mx:    # 최댓값이면 루프 종료
        break
    else:               # 최댓값이 아니면 최댓값이 되도록 처리
        first_v += 1
        mx -= 1
        heappush(others, -mx)

    cnt += 1

print(cnt)

'''
list의 메서드를 이용해서 구현

import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    global cnt

    if len(data) <= 1:
        return

    mx_v = max(data[1:])
    while data[0] <= mx_v:
        data[data[1:].index(mx_v) + 1] -= 1
        data[0] += 1
        mx_v = max(data[1:])
        cnt += 1


N = int(input())
data = [0] * N
for i in range(N):
    data[i] = int(input())

cnt = 0
solve()

print(cnt)
'''