st = input()
N = len(st)

st_set = set()
for n in range(1, N + 1):
    for i in range(0, N - n + 1):
        st_set.add(st[i:i + n])

print(len(st_set))