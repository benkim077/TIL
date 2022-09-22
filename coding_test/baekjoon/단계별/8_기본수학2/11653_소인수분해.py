N = int(input())

if N == 1:
    exit()

i = 2
while i < N:
    if N % i == 0:
        print(i)
        N = N // i
    else:
        i += 1
else:
    print(N)
