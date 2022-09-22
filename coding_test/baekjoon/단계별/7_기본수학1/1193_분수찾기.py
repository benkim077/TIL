N = int(input())

k = 1
while True:
    if k * (k + 1) // 2 >= N:
        break
    k += 1

temp = N - (k - 1) * k // 2
if k % 2 == 1:
    print(f'{k + 1 - temp}/{temp}')
else:
    print(f'{temp}/{k + 1 - temp}')