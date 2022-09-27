A, B = map(int, input().split())
data_A = set(map(int, input().split()))
data_B = set(map(int, input().split()))

ans = len(data_A - data_B) + len(data_B - data_A)
print(ans)