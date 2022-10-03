def make_combinations(n, r, s):
    if r == 0:
        print(*c)
    else:
        for i in range(s, n - r + 1):
            c[r - 1] = data[i]
            make_combinations(n, r - 1, i + 1)


data = [1, 2, 3, 4, 5]
N = len(data)
R = 3

c = [0] * R
make_combinations(N, R, 0)