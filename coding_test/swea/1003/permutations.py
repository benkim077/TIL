# 1, 2, 3, 4, 5 중 3개를 뽑아 나열하는 순열
def make_permutations(i, N, R):
    if i == R:
        print(p)
    else:
        for j in range(N):
            if not check[j]:
                check[j] = True
                p[i] = a[j]
                make_permutations(i + 1, N, R)
                check[j] = False


N = 5
R = 3
a = ['h', 'e', 'l', 'l', 'o']
check = [False] * N
p = [0] * R

make_permutations(0, N, R)
