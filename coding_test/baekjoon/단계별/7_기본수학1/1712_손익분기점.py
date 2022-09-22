import sys
sys.stdin = open('input.txt')


A, B, C = map(int, input().split())

if C - B > 0:
    ans = A // (C - B) + 1
elif C - B <= 0:
    ans = -1

print(ans)